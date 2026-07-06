using System.Text.Json;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

if (args.Length < 2)
{
    Console.Error.WriteLine("Usage: RoslynIndexer <repo-path> <output-json>");
    return 1;
}

var repoPath = Path.GetFullPath(args[0]);
var outputPath = Path.GetFullPath(args[1]);
var symbols = new List<object>();

foreach (var file in Directory.EnumerateFiles(repoPath, "*.cs", SearchOption.AllDirectories))
{
    if (file.Contains($"{Path.DirectorySeparatorChar}bin{Path.DirectorySeparatorChar}") ||
        file.Contains($"{Path.DirectorySeparatorChar}obj{Path.DirectorySeparatorChar}") ||
        file.Contains("Migrations"))
        continue;

    var text = await File.ReadAllTextAsync(file);
    var tree = CSharpSyntaxTree.ParseText(text);
    var root = await tree.GetRootAsync();

    var methods = root.DescendantNodes()
        .OfType<MethodDeclarationSyntax>()
        .Where(m => m.Body != null || m.ExpressionBody != null)
        .Select(m => m.Identifier.Text)
        .Distinct()
        .Take(40)
        .ToList();

    var classes = root.DescendantNodes()
        .OfType<ClassDeclarationSyntax>()
        .Where(c => IsRelevantSymbol(c.Identifier.Text))
        .Select(c => c.Identifier.Text)
        .ToList();

    if (classes.Count == 0 && methods.Count == 0)
        continue;

    var rel = Path.GetRelativePath(repoPath, file).Replace('\\', '/');
    symbols.Add(new
    {
        source_file = rel,
        classes,
        methods = methods.Select(m => $"{Path.GetFileNameWithoutExtension(file)}.{m}").ToList()
    });
}

var payload = new { symbols };
Directory.CreateDirectory(Path.GetDirectoryName(outputPath)!);
await File.WriteAllTextAsync(outputPath, JsonSerializer.Serialize(payload, new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"Indexed {symbols.Count} files -> {outputPath}");
return 0;

static bool IsRelevantSymbol(string name) =>
    name.EndsWith("Handler", StringComparison.Ordinal) ||
    name.EndsWith("Controller", StringComparison.Ordinal) ||
    name.EndsWith("Repository", StringComparison.Ordinal) ||
    name.EndsWith("Client", StringComparison.Ordinal) ||
    name.EndsWith("Job", StringComparison.Ordinal) ||
    name.EndsWith("Worker", StringComparison.Ordinal) ||
    name.EndsWith("Service", StringComparison.Ordinal) ||
    name.EndsWith("Validator", StringComparison.Ordinal) ||
    name.EndsWith("Mapper", StringComparison.Ordinal);
