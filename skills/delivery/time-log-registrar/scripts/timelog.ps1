#Requires -Version 5.1
<#
.SYNOPSIS
    CLI para registrar time logs no Azure DevOps (extensão TechsBCN DevOps-TimeLog).

.DESCRIPTION
    Subcomandos: register, list, capacity, resolve-user, identify, whoami

    Requer variável de ambiente ADO_TIMELOG_PAT com escopos Extension Data, Work Items, Graph, Project and Team (Read).

.EXAMPLE
    .\timelog.ps1 identify -Organization aguiabranca -DeveloperEmail dev@empresa.com.br
    .\timelog.ps1 whoami
    .\timelog.ps1 capacity -Organization aguiabranca -Project "Vix - GRLog" -Team "Vix - GRLog Team"
    .\timelog.ps1 register -InputFile ..\examples\plano-template.json -DryRun
    .\timelog.ps1 list -Organization aguiabranca -Date 2026-07-10 -DeveloperEmail dev@empresa.com
#>

[CmdletBinding()]
param(
    [Parameter(Position = 0, Mandatory = $true)]
    [ValidateSet('register', 'list', 'capacity', 'resolve-user', 'identify', 'whoami', 'show', 'delete', 'search')]
    [string]$Command,

    [string]$Organization,
    [string]$Project,
    [string]$Team,
    [string]$Iteration,
    [string]$InputFile,
    [string]$Date,
    [string]$DeveloperEmail,
    [string]$DeveloperName,
    [int]$WorkItemId,
    [string]$DocumentId,
    [switch]$DryRun,
    [switch]$Update,
    [switch]$Clear
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ExtensionPublisher = 'TechsBCN'
$ExtensionName = 'DevOps-TimeLog'
$CollectionName = 'TimeLogData'
$ApiVersion = '7.2-preview.1'
$WorkApiVersion = '7.1'
$GraphApiVersion = '7.1-preview.1'
$ExpectedDailyMinutes = 420

function Get-OptionalProperty {
    param(
        $Object,
        [string]$Name,
        $Default = $null
    )

    if ($null -eq $Object) { return $Default }
    if ($Object.PSObject.Properties.Name -contains $Name) {
        $value = $Object.$Name
        if ($null -ne $value -and -not [string]::IsNullOrWhiteSpace([string]$value)) {
            return $value
        }
    }

    return $Default
}

function Get-DevProfilePath {
    Join-Path $PSScriptRoot '.dev-profile.json'
}

function Get-DevProfile {
    $path = Get-DevProfilePath
    if (-not (Test-Path $path)) { return $null }

    try {
        return Get-Content $path -Raw -Encoding UTF8 | ConvertFrom-Json
    }
    catch {
        Write-Warning "Perfil inválido em $path — execute identify novamente."
        return $null
    }
}

function Save-DevProfile {
    param($Profile)

    $path = Get-DevProfilePath
    $json = $Profile | ConvertTo-Json -Depth 5
    [System.IO.File]::WriteAllText($path, $json, [System.Text.UTF8Encoding]::new($false))
}

function Remove-DevProfile {
    $path = Get-DevProfilePath
    if (Test-Path $path) {
        Remove-Item $path -Force
    }
}

function Get-EntryDeveloperFields {
    param(
        $Entry,
        $Profile
    )

    $email = if ($Entry.PSObject.Properties.Name -contains 'developerEmail') { [string]$Entry.developerEmail } else { '' }
    $name = if ($Entry.PSObject.Properties.Name -contains 'developerName') { [string]$Entry.developerName } else { '' }
    $userId = if ($Entry.PSObject.Properties.Name -contains 'developerUserId') { [string]$Entry.developerUserId } else { '' }

    if ([string]::IsNullOrWhiteSpace($email) -and [string]::IsNullOrWhiteSpace($name) -and [string]::IsNullOrWhiteSpace($userId)) {
        if (-not $Profile) {
            throw @'
Entrada sem desenvolvedor e perfil não configurado.
Configure uma vez com:
  .\timelog.ps1 identify -Organization aguiabranca -DeveloperEmail seu@email.com.br
Depois use planos sem developerEmail/developerUserId (ver examples/plano-perfil.json).
'@
        }

        return @{
            Email       = [string](Get-OptionalProperty -Object $Profile -Name 'developerEmail')
            DisplayName = [string](Get-OptionalProperty -Object $Profile -Name 'developerName')
            UserId      = [string](Get-OptionalProperty -Object $Profile -Name 'developerUserId')
            FromProfile = $true
        }
    }

    return @{
        Email       = $email
        DisplayName = $name
        UserId      = $userId
        FromProfile = $false
    }
}

function Get-Pat {
    $pat = $env:ADO_TIMELOG_PAT
    if ([string]::IsNullOrWhiteSpace($pat)) {
        $pat = [Environment]::GetEnvironmentVariable('ADO_TIMELOG_PAT', 'User')
    }
    if ([string]::IsNullOrWhiteSpace($pat)) {
        $patFile = Join-Path $PSScriptRoot '.ado-timelog-pat'
        if (Test-Path $patFile) {
            $pat = (Get-Content $patFile -Raw).Trim()
        }
    }
    return $pat
}

function Get-AdoAuthHeader {
    $pat = Get-Pat
    if (-not [string]::IsNullOrWhiteSpace($pat)) {
        $pair = ":$pat"
        $bytes = [System.Text.Encoding]::ASCII.GetBytes($pair)
        $token = [Convert]::ToBase64String($bytes)
        return @{ Authorization = "Basic $token" }
    }

    $azToken = az account get-access-token --resource 499b84ac-1321-427f-aa17-267ca6975798 --query accessToken -o tsv 2>$null
    if (-not [string]::IsNullOrWhiteSpace($azToken)) {
        return @{ Authorization = "Bearer $azToken" }
    }

    throw 'Defina ADO_TIMELOG_PAT, crie scripts/.ado-timelog-pat, ou execute az login.'
}

function Get-BasicAuthHeader {
    return Get-AdoAuthHeader
}

function Invoke-AdoRest {
    param(
        [string]$Method = 'GET',
        [string]$Uri,
        $Body
    )

    $headers = Get-BasicAuthHeader
    $params = @{
        Method  = $Method
        Uri     = $Uri
        Headers = $headers
    }

    if ($null -ne $Body) {
        $jsonBody = $Body | ConvertTo-Json -Depth 10 -Compress
        $params['ContentType'] = 'application/json; charset=utf-8'
        $params['Body'] = [System.Text.Encoding]::UTF8.GetBytes($jsonBody)
    }

    return Invoke-RestMethod @params
}

function Get-IsoWeekString {
    param([datetime]$DateTime)
    $culture = [System.Globalization.CultureInfo]::InvariantCulture
    $calendar = $culture.Calendar
    $week = $calendar.GetWeekOfYear($DateTime, [System.Globalization.CalendarWeekRule]::FirstFourDayWeek, [DayOfWeek]::Monday)
    return '{0}-W{1:D2}' -f $DateTime.Year, $week
}

function Get-TimeLogBaseUrl {
    param([string]$Org)
    "https://extmgmt.dev.azure.com/$Org/_apis/ExtensionManagement/InstalledExtensions/$ExtensionPublisher/$ExtensionName/Data/Scopes/Default/Current/Collections/$CollectionName"
}

function Get-AllTimeLogDocuments {
    param([string]$Org)
    $url = "$(Get-TimeLogBaseUrl -Org $Org)/Documents?api-version=$ApiVersion"
    $result = Invoke-AdoRest -Uri $url
    return Get-ApiCollection $result
}

function Get-ApiCollection {
    param($Result)

    if ($null -eq $Result) { return @() }
    if ($Result.PSObject.Properties.Name -contains 'value') {
        return @($Result.value)
    }
    if ($Result -is [array]) { return $Result }
    return @($Result)
}

function Get-IdentityPropertyValue {
    param(
        $Identity,
        [string]$PropertyName
    )

    if ($null -eq $Identity -or -not $Identity.properties) { return $null }
    if ($Identity.properties.PSObject.Properties.Name -notcontains $PropertyName) { return $null }

    $prop = $Identity.properties.$PropertyName
    if ($null -eq $prop) { return $null }
    if ($prop -is [string]) { return $prop }
    if ($prop.PSObject.Properties.Name -contains 'value' -and $prop.value) {
        return [string]$prop.value
    }

    return [string]$prop
}

function Test-EmailEquals {
    param(
        [string]$Left,
        [string]$Right
    )

    if ([string]::IsNullOrWhiteSpace($Left) -or [string]::IsNullOrWhiteSpace($Right)) { return $false }
    return $Left.Trim().ToLowerInvariant() -eq $Right.Trim().ToLowerInvariant()
}

function Get-IdentityDisplayName {
    param($Identity)

    if ($null -eq $Identity) { return $null }

    foreach ($prop in @('customDisplayName', 'displayName', 'providerDisplayName')) {
        if ($Identity.PSObject.Properties.Name -contains $prop -and -not [string]::IsNullOrWhiteSpace($Identity.$prop)) {
            return [string]$Identity.$prop
        }
    }

    return $null
}

function Get-IdentityByOriginId {
    param(
        [string]$Org,
        [string]$OriginId
    )

    if ([string]::IsNullOrWhiteSpace($OriginId)) { return $null }

    $url = "https://vssps.dev.azure.com/$Org/_apis/identities?identityIds=$OriginId&api-version=6.0"
    try {
        $identity = Get-ApiCollection (Invoke-AdoRest -Uri $url) | Select-Object -First 1
        if ($identity) { return $identity }
    }
    catch { }

    return $null
}

function Get-IdentityByEmail {
    param(
        [string]$Org,
        [string]$Email
    )

    if ([string]::IsNullOrWhiteSpace($Email)) { return $null }

    $url = "https://vssps.dev.azure.com/$Org/_apis/identities?searchFilter=General&filterValue=$([uri]::EscapeDataString($Email))&queryMembership=None&api-version=6.0"
    try {
        $results = Get-ApiCollection (Invoke-AdoRest -Uri $url)
        $match = $results | Where-Object {
            Test-EmailEquals -Left (Get-IdentityEmail -Identity $_ -Fallback '') -Right $Email
        } | Select-Object -First 1

        if (-not $match -and $Email.Contains('@') -and $results.Count -ge 1) {
            # Busca por e-mail completo na Identities API — primeiro resultado é o usuário correto
            $match = $results[0]
        }

        return $match
    }
    catch { }

    return $null
}

function Get-GraphUserByEmail {
    param(
        [string]$Org,
        [string]$Email
    )

    if ([string]::IsNullOrWhiteSpace($Email)) { return $null }

    $url = "https://vssps.dev.azure.com/$Org/_apis/graph/users?api-version=$GraphApiVersion&filterValue=$([uri]::EscapeDataString($Email))&filterType=MailAddress"
    try {
        $results = Get-ApiCollection (Invoke-AdoRest -Uri $url)
        return $results | Where-Object { Test-EmailEquals -Left $_.mailAddress -Right $Email } | Select-Object -First 1
    }
    catch { }

    return $null
}

function Resolve-IdentityByEmail {
    param(
        [string]$Org,
        [string]$Email
    )

    $identity = Get-IdentityByEmail -Org $Org -Email $Email
    $graphUser = Get-GraphUserByEmail -Org $Org -Email $Email

    if (-not $identity -and -not $graphUser) { return $null }

    $userId = $null
    $displayName = $null
    $resolvedEmail = $Email

    if ($identity) {
        $displayName = Get-IdentityDisplayName -Identity $identity
        if ($identity.PSObject.Properties.Name -contains 'id' -and $identity.id) {
            $userId = [string]$identity.id
        }
        $resolvedEmail = Get-IdentityEmail -Identity $identity -Fallback $Email
    }

    if ($graphUser) {
        if ($graphUser.displayName) { $displayName = [string]$graphUser.displayName }
        if ($graphUser.mailAddress) { $resolvedEmail = [string]$graphUser.mailAddress }
        if (-not $userId -and -not $identity -and $graphUser.originId) {
            $userId = [string]$graphUser.originId
        }
    }

    if ([string]::IsNullOrWhiteSpace($displayName) -or [string]::IsNullOrWhiteSpace($userId)) { return $null }

    return @{
        UserId      = $userId
        DisplayName = $displayName
        Email       = $resolvedEmail
    }
}

function Get-GraphUserByOriginId {
    param(
        [string]$Org,
        [string]$OriginId
    )

    $identity = Get-IdentityByOriginId -Org $Org -OriginId $OriginId
    if ($identity) { return $identity }

    $graphUrl = "https://vssps.dev.azure.com/$Org/_apis/graph/users?api-version=$GraphApiVersion"
    $all = Get-ApiCollection (Invoke-AdoRest -Uri $graphUrl)
    return $all | Where-Object { $_.originId -eq $OriginId } | Select-Object -First 1
}

function Get-IdentityEmail {
    param($Identity, [string]$Fallback = '')

    if ($null -eq $Identity) { return $Fallback }

    if ($Identity.PSObject.Properties.Name -contains 'mailAddress' -and $Identity.mailAddress) {
        return [string]$Identity.mailAddress
    }

    foreach ($prop in @('Mail', 'Account')) {
        $value = Get-IdentityPropertyValue -Identity $Identity -PropertyName $prop
        if (-not [string]::IsNullOrWhiteSpace($value)) { return $value }
    }

    if ($Identity.PSObject.Properties.Name -contains 'uniqueName' -and $Identity.uniqueName) {
        return [string]$Identity.uniqueName
    }

    return $Fallback
}

function Get-WorkItemFromApi {
    param(
        [string]$Org,
        [int]$Id
    )

    $url = "https://dev.azure.com/$Org/_apis/wit/workitems/$Id`?api-version=$WorkApiVersion"
    return Invoke-AdoRest -Uri $url
}

function Get-WorkItemAssignedIdentity {
    param(
        [string]$Org,
        [int]$Id
    )

    try {
        $wi = Get-WorkItemFromApi -Org $Org -Id $Id
        $assigned = $wi.fields.'System.AssignedTo'
        if ($assigned) {
            return @{
                DisplayName = [string]$assigned.displayName
                Email       = [string]$assigned.uniqueName
                UserId      = [string]$assigned.id
            }
        }
    }
    catch { }

    return $null
}

function Resolve-DeveloperIdentity {
    param(
        [string]$Org,
        [string]$Email,
        [string]$DisplayName,
        [string]$UserId,
        [int]$WorkItemId = 0
    )

    $resolved = $null

    if (-not [string]::IsNullOrWhiteSpace($UserId)) {
        $byId = Get-IdentityByOriginId -Org $Org -OriginId $UserId
        $resolvedName = Get-IdentityDisplayName -Identity $byId
        if ($resolvedName) {
            $resolved = @{
                UserId      = $UserId
                DisplayName = $resolvedName
                Email       = Get-IdentityEmail -Identity $byId -Fallback $Email
            }
        }
        elseif (-not $resolved) {
            $graphUser = Get-GraphUserByOriginId -Org $Org -OriginId $UserId
            $resolvedName = Get-IdentityDisplayName -Identity $graphUser
            if ($resolvedName) {
                $resolved = @{
                    UserId      = $UserId
                    DisplayName = $resolvedName
                    Email       = Get-IdentityEmail -Identity $graphUser -Fallback $Email
                }
            }
        }
    }

    if (-not $resolved -and -not [string]::IsNullOrWhiteSpace($Email)) {
        $byEmail = Resolve-IdentityByEmail -Org $Org -Email $Email
        if ($byEmail) {
            $resolved = @{
                UserId      = $byEmail.UserId
                DisplayName = $byEmail.DisplayName
                Email       = $byEmail.Email
            }
        }
    }

    if ($WorkItemId -gt 0) {
        $assigned = Get-WorkItemAssignedIdentity -Org $Org -Id $WorkItemId
        if ($assigned) {
            $matchesUser = (
                ($Email -and (Test-EmailEquals -Left $assigned.Email -Right $Email)) -or
                ($UserId -and $assigned.UserId -eq $UserId) -or
                ($resolved -and (Test-EmailEquals -Left $assigned.Email -Right $resolved.Email)) -or
                ($resolved -and $assigned.UserId -eq $resolved.UserId)
            )
            if ($matchesUser) {
                if ($resolved) {
                    $resolved.DisplayName = $assigned.DisplayName
                    if (-not $resolved.Email) { $resolved.Email = $assigned.Email }
                    if (-not $resolved.UserId) { $resolved.UserId = $assigned.UserId }
                }
                else {
                    $resolved = @{
                        UserId      = $assigned.UserId
                        DisplayName = $assigned.DisplayName
                        Email       = $assigned.Email
                    }
                }
            }
        }
    }

    if ($resolved) { return $resolved }

    $base = "https://vssps.dev.azure.com/$Org/_apis/graph/users?api-version=$GraphApiVersion"

    if (-not [string]::IsNullOrWhiteSpace($DisplayName)) {
        Write-Warning 'Busca por nome pode retornar usuário errado. Prefira -DeveloperEmail.'
        $url = "$base&filterValue=$([uri]::EscapeDataString($DisplayName))&filterType=DisplayName"
        $found = Get-ApiCollection (Invoke-AdoRest -Uri $url)
        $exact = $found | Where-Object {
            (Test-EmailEquals -Left $_.displayName -Right $DisplayName) -or
            (Test-EmailEquals -Left $_.customDisplayName -Right $DisplayName)
        }
        $match = $exact | Select-Object -First 1
        if (-not $match) {
            $partial = @($found | Where-Object {
                    ($_.displayName -and $_.displayName -like "*$DisplayName*") -or
                    ($_.customDisplayName -and $_.customDisplayName -like "*$DisplayName*")
                })
            if ($partial.Count -eq 1) {
                $match = $partial[0]
            }
            elseif ($partial.Count -gt 1) {
                throw "Ambíguo: $($partial.Count) usuários para '$DisplayName'. Use -DeveloperEmail."
            }
        }
        if ($match) {
            $matchEmail = Get-IdentityEmail -Identity $match -Fallback $Email
            if ($matchEmail) {
                $byEmail = Resolve-IdentityByEmail -Org $Org -Email $matchEmail
                if ($byEmail) { return $byEmail }
            }
            return @{
                UserId      = if ($match.PSObject.Properties.Name -contains 'id' -and $match.id) { [string]$match.id } elseif ($match.originId) { [string]$match.originId } else { $UserId }
                DisplayName = Get-IdentityDisplayName -Identity $match
                Email       = $matchEmail
            }
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($UserId)) {
        return @{
            UserId      = $UserId
            DisplayName = if ($DisplayName) { $DisplayName } elseif ($Email) { $Email } else { $UserId }
            Email       = $Email
        }
    }

    throw "Usuário não encontrado: email='$Email' displayName='$DisplayName' userId='$UserId'"
}

function Test-WorkItemExists {
    param(
        [string]$Org,
        [int]$Id
    )

    try {
        $wi = Get-WorkItemFromApi -Org $Org -Id $Id
        return @{
            Id    = $wi.id
            Title = $wi.fields.'System.Title'
            Type  = $wi.fields.'System.WorkItemType'
        }
    }
    catch {
        Write-Warning "Não foi possível validar work item $Id ($($_.Exception.Message)). Prosseguindo com o ID informado."
        return @{
            Id    = $Id
            Title = "Work Item $Id"
            Type  = '(não validado)'
        }
    }
}

function Get-IterationId {
    param(
        [string]$Org,
        [string]$Project,
        [string]$Team,
        [string]$IterationName
    )

    $teamSegment = if ($Team) { "/$([uri]::EscapeDataString($Team))" } else { '' }
    $url = "https://dev.azure.com/$Org/$([uri]::EscapeDataString($Project))$teamSegment/_apis/work/teamsettings/iterations?api-version=$WorkApiVersion"
    $result = Invoke-AdoRest -Uri $url

    if ($IterationName) {
        $iterations = Get-ApiCollection $result
        $match = $iterations | Where-Object { $_.name -eq $IterationName } | Select-Object -First 1
        if (-not $match) {
            throw "Iteration '$IterationName' não encontrada"
        }
        return $match.id
    }

    $iterations = Get-ApiCollection $result
    $current = $iterations | Where-Object { $_.attributes.timeFrame -eq 'current' } | Select-Object -First 1
    if ($current) { return $current.id }

    throw 'Nenhuma iteration atual encontrada. Informe -Iteration explicitamente.'
}

function Resolve-EntryDuration {
    param($Entry)

    $hasHours = $Entry.PSObject.Properties.Name -contains 'hours'
    $hasMinutes = $Entry.PSObject.Properties.Name -contains 'minutes'

    if ($Entry.PSObject.Properties.Name -contains 'time') {
        $total = [int]$Entry.time
        $hours = [math]::Floor($total / 60)
        $durationMinutes = $total % 60
    }
    elseif ($hasHours) {
        $hours = [int]$Entry.hours
        $durationMinutes = if ($hasMinutes) { [int]$Entry.minutes } else { 0 }
    }
    elseif ($hasMinutes) {
        $total = [int]$Entry.minutes
        $hours = [math]::Floor($total / 60)
        $durationMinutes = $total % 60
    }
    else {
        throw 'Entrada sem duração: informe hours + minutes (como na tela) ou minutes (total).'
    }

    return @{
        Hours             = $hours
        DurationMinutes   = $durationMinutes
        TotalMinutes      = ($hours * 60) + $durationMinutes
        StartTime         = if ($Entry.PSObject.Properties.Name -contains 'startTime') { [string]$Entry.startTime } else { '09:00' }
    }
}

function Build-TimeLogDocument {
    param(
        $Item,
        [string]$Date
    )

    $startTime = if ([string]::IsNullOrWhiteSpace($Item.StartTime)) { '' } else { $Item.StartTime }
    $dateValue = if ($startTime) { "$Date $startTime" } else { $Date }

    return @{
        workItemId   = $Item.WorkItemId
        workItemName = $Item.WorkItemTitle
        userId       = $Item.UserId
        user         = $Item.Developer
        type         = $Item.Activity
        time         = $Item.TotalMinutes
        startTime    = $startTime
        date         = $dateValue
        notes        = $Item.Notes
    }
}

function Invoke-RegisterCommand {
    if (-not $InputFile) { throw 'register requer -InputFile' }
    if (-not (Test-Path $InputFile)) { throw "Arquivo não encontrado: $InputFile" }

    $plan = Get-Content $InputFile -Raw -Encoding UTF8 | ConvertFrom-Json
    $profile = Get-DevProfile
    $org = Get-OptionalProperty -Object $plan -Name 'organization' -Default $Organization
    if (-not $org) { $org = Get-OptionalProperty -Object $profile -Name 'organization' }
    if (-not $org) { throw 'organization obrigatória no JSON, via -Organization, ou no perfil (identify)' }

    $entries = @($plan.entries)
    if ($entries.Count -eq 0) { throw 'Nenhuma entrada no plano' }

    $date = Get-OptionalProperty -Object $plan -Name 'date' -Default $Date
    if (-not $date) { $date = Get-Date -Format 'yyyy-MM-dd' }

    $resolved = @()
    $identityCache = @{}

    foreach ($entry in $entries) {
        $fields = Get-EntryDeveloperFields -Entry $entry -Profile $profile
        $email = $fields.Email
        $name = $fields.DisplayName
        $userId = $fields.UserId
        $cacheKey = if ($userId) { $userId } elseif ($email) { $email.ToLower() } else { $name }

        if (-not $identityCache.ContainsKey($cacheKey)) {
            if ($fields.FromProfile) {
                $identityCache[$cacheKey] = @{
                    UserId      = $userId
                    DisplayName = $name
                    Email       = $email
                }
            }
            else {
                $identityCache[$cacheKey] = Resolve-DeveloperIdentity -Org $org -Email $email -DisplayName $name -UserId $userId -WorkItemId ([int]$entry.workItemId)
            }
        }
        $identity = $identityCache[$cacheKey]

        $wi = Test-WorkItemExists -Org $org -Id ([int]$entry.workItemId)
        $duration = Resolve-EntryDuration -Entry $entry

        $resolved += [pscustomobject]@{
            Developer       = $identity.DisplayName
            Email           = $identity.Email
            UserId          = $identity.UserId
            WorkItemId      = [int]$entry.workItemId
            WorkItemTitle   = $wi.Title
            Activity        = $entry.activity
            Hours           = $duration.Hours
            DurationMinutes = $duration.DurationMinutes
            TotalMinutes    = $duration.TotalMinutes
            StartTime       = $duration.StartTime
            Notes           = if ($entry.PSObject.Properties.Name -contains 'notes') { [string]$entry.notes } else { '' }
            Id              = if ($entry.PSObject.Properties.Name -contains 'id') { $entry.id } else { $null }
            Etag            = if ($entry.PSObject.Properties.Name -contains '__etag') { $entry.__etag } else { $null }
        }
    }

    $grouped = $resolved | Group-Object { "$($_.Email)|$date" }
    foreach ($group in $grouped) {
        $total = ($group.Group | Measure-Object -Property TotalMinutes -Sum).Sum
        if ($total -ne $ExpectedDailyMinutes) {
            Write-Warning "Total de $($group.Group[0].Developer) em $date = $($total) min (esperado $ExpectedDailyMinutes)"
        }
    }

    Write-Host ''
    Write-Host '=== PREVIEW ===' -ForegroundColor Cyan
    $resolved | Format-Table Developer, WorkItemId, Activity, @{N='Time';E={ '{0}:{1:D2}' -f $_.Hours, $_.DurationMinutes }}, @{N='Start';E={$_.StartTime}}, Notes -AutoSize

    if ($DryRun) {
        Write-Host 'DryRun: nenhuma alteração gravada.' -ForegroundColor Yellow
        return
    }

    $base = Get-TimeLogBaseUrl -Org $org
    $created = 0
    $updated = 0

    foreach ($item in $resolved) {
        $doc = Build-TimeLogDocument -Item $item -Date $date

        if ($Update -and $item.Id) {
            $doc['id'] = $item.Id
            $doc['__etag'] = $item.Etag
            $url = "$base/Documents/$($item.Id)`?api-version=$ApiVersion"
            Invoke-AdoRest -Method PUT -Uri $url -Body $doc | Out-Null
            $updated++
            Write-Host "Atualizada $($item.Id) — $($item.Developer) — WI $($item.WorkItemId) — $($item.Activity)" -ForegroundColor Green
        }
        else {
            $newId = [guid]::NewGuid().ToString()
            $doc['id'] = $newId
            $url = "$base/Documents?api-version=$ApiVersion"
            Invoke-AdoRest -Method POST -Uri $url -Body $doc | Out-Null
            $created++
            Write-Host "Criada $newId — $($item.Developer) — WI $($item.WorkItemId) — $($item.Activity) — $($item.Hours):$('{0:D2}' -f $item.DurationMinutes)" -ForegroundColor Green
        }
    }

    Write-Host ''
    Write-Host "$created criada(s), $updated atualizada(s)." -ForegroundColor Cyan
}

function Invoke-ListCommand {
    $org = $Organization
    if (-not $org) {
        $profile = Get-DevProfile
        $org = Get-OptionalProperty -Object $profile -Name 'organization'
    }
    if (-not $org) { throw 'list requer -Organization' }
    if (-not $Date) { throw 'list requer -Date (yyyy-MM-dd)' }

    $profile = Get-DevProfile
    $email = $DeveloperEmail
    if (-not $email) {
        $email = Get-OptionalProperty -Object $profile -Name 'developerEmail'
    }

    $docs = Get-AllTimeLogDocuments -Org $org
    $filtered = @($docs | Where-Object { $_.date -eq $Date -or $_.date -like "$Date *" })

    if ($email) {
        $profileEmail = Get-OptionalProperty -Object $profile -Name 'developerEmail'
        $profileUserId = Get-OptionalProperty -Object $profile -Name 'developerUserId'
        if ($profileEmail -eq $email -and $profileUserId) {
            $userId = $profileUserId
        }
        else {
            $identity = Resolve-DeveloperIdentity -Org $org -Email $email
            $userId = $identity.UserId
        }
        $filtered = @($filtered | Where-Object { $_.userId -eq $userId })
    }

    if ($WorkItemId) {
        $filtered = @($filtered | Where-Object { $_.workItemId -eq $WorkItemId })
    }

    if ($filtered.Count -eq 0) {
        Write-Host 'Nenhuma entrada encontrada.'
        return
    }

    $filtered | Select-Object id, date, startTime, time, user, workItemId, type, notes, __etag |
        Format-Table -AutoSize
}

function Invoke-CapacityCommand {
    if (-not $Organization -or -not $Project) {
        throw 'capacity requer -Organization e -Project'
    }

    $iterationId = Get-IterationId -Org $Organization -Project $Project -Team $Team -IterationName $Iteration
    $teamSegment = if ($Team) { "/$([uri]::EscapeDataString($Team))" } else { '' }
    $url = "https://dev.azure.com/$Organization/$([uri]::EscapeDataString($Project))$teamSegment/_apis/work/teamsettings/iterations/$iterationId/capacities?api-version=$WorkApiVersion"
    $result = Invoke-AdoRest -Uri $url

    $rows = @()
    foreach ($member in $result.teamMembers) {
        $capPerDay = ($member.activities | Measure-Object -Property capacityPerDay -Sum).Sum
        if ($capPerDay -gt 0) {
            $rows += [pscustomobject]@{
                DisplayName    = $member.teamMember.displayName
                Email          = $member.teamMember.uniqueName
                TeamMemberId   = $member.teamMember.id
                CapacityPerDay = $capPerDay
            }
        }
    }

    if ($rows.Count -eq 0) {
        Write-Host 'Nenhum membro com capacity > 0.'
        return
    }

    $rows | Format-Table -AutoSize
}

function Invoke-DeleteCommand {
    if (-not $Organization) { throw 'delete requer -Organization' }
    if (-not $DocumentId) { throw 'delete requer -DocumentId' }

    $base = Get-TimeLogBaseUrl -Org $Organization
    $url = "$base/Documents/${DocumentId}`?api-version=$ApiVersion"
    Invoke-AdoRest -Method DELETE -Uri $url | Out-Null
    Write-Host "Excluída $DocumentId" -ForegroundColor Green
}

function Invoke-SearchCommand {
    if (-not $Organization) { throw 'search requer -Organization' }

    $all = Get-AllTimeLogDocuments -Org $Organization
    if ($WorkItemId) {
        $all = @($all | Where-Object { $_.workItemId -eq $WorkItemId })
    }
    if ($DeveloperEmail) {
        $identity = Resolve-DeveloperIdentity -Org $Organization -Email $DeveloperEmail
        $all = @($all | Where-Object { $_.userId -eq $identity.UserId })
    }

    $all | Select-Object -First 20 id, date, startTime, time, user, workItemId, type, notes |
        Format-Table -AutoSize
}

function Invoke-ShowCommand {
    if (-not $Organization) { throw 'show requer -Organization' }
    if (-not $DocumentId) { throw 'show requer -DocumentId' }

    $base = Get-TimeLogBaseUrl -Org $Organization
    $url = "$base/Documents/${DocumentId}`?api-version=$ApiVersion"
    $doc = Invoke-AdoRest -Uri $url
    $doc | ConvertTo-Json -Depth 8
}

function Invoke-ResolveUserCommand {
    if (-not $Organization) { throw 'resolve-user requer -Organization' }
    if (-not $DeveloperEmail -and -not $DeveloperName) { throw 'resolve-user requer -DeveloperEmail ou -DeveloperName' }

    $identity = Resolve-DeveloperIdentity -Org $Organization -Email $DeveloperEmail -DisplayName $DeveloperName
    $identity | Format-List
}

function Invoke-IdentifyCommand {
    if ($Clear) {
        Remove-DevProfile
        Write-Host 'Perfil removido.' -ForegroundColor Yellow
        return
    }

    if (-not $Organization) { throw 'identify requer -Organization' }
    if (-not $DeveloperEmail -and -not $DeveloperName) {
        throw 'identify requer -DeveloperEmail (recomendado) ou -DeveloperName'
    }

    if ($DeveloperName -and -not $DeveloperEmail) {
        Write-Warning 'Busca por nome pode retornar usuário errado. Prefira -DeveloperEmail.'
    }

    $identity = Resolve-DeveloperIdentity -Org $Organization -Email $DeveloperEmail -DisplayName $DeveloperName

    $profile = [ordered]@{
        organization      = $Organization
        developerEmail    = $identity.Email
        developerUserId   = $identity.UserId
        developerName     = $identity.DisplayName
        savedAt           = (Get-Date).ToString('o')
    }

    Save-DevProfile -Profile $profile

    Write-Host ''
    Write-Host "Perfil salvo em $(Get-DevProfilePath)" -ForegroundColor Green
    Write-Host 'Próximos registros podem omitir developerEmail/developerUserId no JSON.' -ForegroundColor Cyan
    Write-Host ''
    $profile | Format-List
}

function Invoke-WhoamiCommand {
    $profile = Get-DevProfile
    if (-not $profile) {
        Write-Host 'Nenhum perfil configurado.'
        Write-Host ''
        Write-Host 'Configure com:'
        Write-Host '  .\timelog.ps1 identify -Organization aguiabranca -DeveloperEmail seu@email.com.br' -ForegroundColor Cyan
        return
    }

    Write-Host 'Perfil ativo:' -ForegroundColor Cyan
    $profile | Format-List
}

switch ($Command) {
    'register' { Invoke-RegisterCommand }
    'list' { Invoke-ListCommand }
    'capacity' { Invoke-CapacityCommand }
    'resolve-user' { Invoke-ResolveUserCommand }
    'identify' { Invoke-IdentifyCommand }
    'whoami' { Invoke-WhoamiCommand }
    'show' { Invoke-ShowCommand }
    'delete' { Invoke-DeleteCommand }
    'search' { Invoke-SearchCommand }
}
