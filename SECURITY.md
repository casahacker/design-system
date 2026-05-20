# Política de Segurança

## Versões suportadas

| Versão | Suportada |
|---|---|
| 1.x | ✓ |
| 0.x | ✗ |

## Reportando uma vulnerabilidade

**Não abra issue pública** pra vulnerabilidades de segurança. Em vez disso:

1. Use o [Security Advisory privado do GitHub](https://github.com/casahacker/design-system/security/advisories/new)
2. Ou envie email pra contato@casahacker.org com `[security]` no assunto

Inclua:
- Descrição da vulnerabilidade
- Passos pra reproduzir
- Impacto potencial
- Sugestão de fix (opcional)

## Resposta esperada

- **24h** — confirmação de recebimento
- **7d** — avaliação inicial + classificação de severidade
- **30d** — patch lançado (vulnerabilidades críticas mais rápido)

## Reconhecimento

Pesquisadores que reportam responsavelmente são creditados no changelog (se quiserem) e mencionados em security advisories.

## Escopo

Este DS é HTML/CSS/JS estático. Vulnerabilidades comuns:
- XSS via conteúdo injetado no HTML
- Vulnerabilidades em deps CDN (barra-acessibilidade, fontes)
- Path traversal / typosquatting nos generators Python

Fora de escopo:
- Vulnerabilidades em sites de terceiros que linkamos
- Issues de produção em sites que USAM o CHDS (reporte ao mantenedor do produto)
