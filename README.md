# kb-midia

Mídia dos posts da @karen.sbarrosnutri, hospedada aqui para o Metricool usar como link direto.

## Regra principal: nada vai ao ar sem aprovação

1. **Rascunho:** cada post é criado num canvas editável no Claude, onde você edita texto, cor e layout.
2. **Aprovação:** só depois do seu "aprovado" para aquele post específico o resto acontece.
3. **Arte final:** as artes aprovadas viram PNG e entram neste repositório.
4. **Metricool:** o post é criado como **rascunho para revisão**. Agendar ou publicar exige um novo ok seu, com data e hora confirmadas.

Aprovação vale por post. Um ok não libera os seguintes.

## Pastas

| Pasta | O que tem |
|---|---|
| `posts/AAAA-MM-DD_tema/` | Fonte de cada post: `slides.html` (as artes) e `legenda.md` (legenda, comentário fixado, checklist) |
| `carrossel/AAAA-MM/` | PNGs 1080×1350 dos carrosséis aprovados |
| `reels/AAAA-MM/` | Capas e textos de reel (1080×1920) |
| `stories/AAAA-MM/` | Stories (1080×1920) |
| `capas/AAAA-MM/` | Capas avulsas para o grid |
| `design/` | Cores, fontes e classes do design system da Karen |
| `gerador/` | Script que transforma `slides.html` em PNG |

Nome dos arquivos: `AAAA-MM-DD_tema_NN.png`, por exemplo `2026-10-14_pre-treino-mounjaro_01.png`.

## Link para o Metricool

Cada arquivo tem um link direto neste formato:

```
https://raw.githubusercontent.com/lucasgiordane/kb-midia/main/<pasta>/<arquivo>
```

Exemplo: `https://raw.githubusercontent.com/lucasgiordane/kb-midia/main/carrossel/2026-10/2026-10-14_pre-treino-mounjaro_01.png`

## O repositório é público

Qualquer pessoa com o link vê o arquivo. Nunca colocar aqui:
- prints de conversa
- depoimentos ou fotos de paciente
- documentos
- nada que identifique alguém

Prova social autorizada só entra como arte final aprovada.

## Gerar as artes

```
python3 gerador/render.py posts/2026-10-14_pre-treino-mounjaro
```

Precisa de Python com Playwright e Chromium. Cada `.kb-arte` do `slides.html` vira um PNG na pasta do tipo indicado em `data-tipo` no `<body>`.
