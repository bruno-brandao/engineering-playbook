# Checklist — Pre-PR Reviewer

## Escopo

- [ ] Branch-base confirmada
- [ ] Status e diff revisados
- [ ] Arquivos inesperados, gerados ou sensíveis avaliados
- [ ] Escopo mapeado para US/plano quando disponível

## Verificação

- [ ] `local-verification` carregada ou ausência declarada
- [ ] Comandos têm origem comprovada
- [ ] Lint/format avaliado conforme projeto
- [ ] Typecheck/compile avaliado conforme projeto
- [ ] Build avaliado conforme projeto
- [ ] Testes aplicáveis executados
- [ ] Falhas e checks não executados foram diferenciados

## Risco

- [ ] Regressões relacionadas avaliadas
- [ ] Contratos e integrações avaliados
- [ ] Migrations/rollback avaliados quando aplicáveis
- [ ] Segurança, secrets e autorização avaliados
- [ ] UI, acessibilidade e observabilidade avaliadas quando aplicáveis

## Saída

- [ ] Evidências citadas
- [ ] Ressalvas possuem responsável/aceite
- [ ] Veredito segue os critérios da skill
- [ ] Nenhuma correção, commit, push ou PR foi feito automaticamente
