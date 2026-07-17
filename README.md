# Context Dependency in LLM-Based Requirements Clarification

Este repositório é o **replication package** de uma replicação quantitativa dos
efeitos de contexto na clarificação de requisitos baseada em LLMs. Ele reúne o
**frozen analysis dataset** (planilha congelada), o **notebook** de análise, os
artefatos de execução, os materiais de anotação e os resultados exportados.

O objetivo deste README é ajudar um professor, revisor ou leitor iniciante a
entender: (1) o que foi executado, (2) quais dados foram produzidos, (3) como as
perguntas foram limpas e anotadas, (4) como os gaps foram normalizados, (5) como
a adjudicação foi usada, (6) como o notebook reproduz as estatísticas e (7) quais
arquivos suportam cada tabela do artigo.

---

## Visão geral do experimento

O estudo investiga como diferentes tipos de contexto afetam as perguntas de
clarificação geradas por um agente de **Specification-Driven Development (SDD)**
baseado em LLM. O agente foi observado por meio do comando:

```text
/speckit.clarify
```

A pergunta central é se fornecer diferentes tipos de contexto ao agente
**reduz, desloca ou revela** lacunas de clarificação em User Stories.

A variável dependente principal é:

```text
necessary_unanswered
```

Uma lacuna conta como `necessary_unanswered` quando é, simultaneamente:

- `Final_Coverage == "Unanswered"`
- `Final_Relevance == "Necessary"`

Ou seja, é uma lacuna **funcionalmente necessária** que permaneceu **sem
resposta** no material fornecido ao agente.

---

## Desenho experimental

O experimento usa:

- 4 User Stories;
- 6 context conditions (condições contextuais);
- 5 repetições independentes por combinação User Story × condition;
- 120 execuções válidas no total.

```text
4 User Stories × 6 context conditions × 5 repetitions = 120 executions
```

As quatro User Stories:

| ID | Domain | Main functionality |
| --- | --- | --- |
| US02 | Waste management | Search nearby facilities |
| US08 | Agile estimation | Reveal estimates simultaneously |
| US19 | Training management | Join a waiting list |
| US22 | Content recommendation | Recommend content based on similar profiles |

As seis context conditions:

| Condition | Material provided to the agent |
| --- | --- |
| C0 | User Story only |
| CL | User Story + lexical context |
| CO | User Story + operational context |
| CD | User Story + decisional context |
| CS | User Story + systemic context |
| CT | User Story + CL + CO + CD + CS |

- **C0** é a condição de controle, sem contexto adicional.
- **CL** fornece definições lexicais e significados de termos.
- **CO** fornece regras operacionais, exceções, estados e comportamento esperado.
- **CD** fornece decisões de produto, escopo e alternativas escolhidas.
- **CS** fornece informações sistêmicas, como atores, fontes de dados, serviços e
  dependências.
- **CT** combina todos os tipos de contexto.

---

## Execução do experimento

Cada combinação User Story × condition foi executada 5 vezes de forma
independente. Cada execução recebeu um identificador `Run_ID`, por exemplo:

```text
US02_C0_R1
US02_C0_R2
US02_CL_R1
US22_CT_R5
```

O formato geral é:

```text
<UserStory>_<Condition>_R<Repetition>
```

As execuções foram randomizadas antes da coleta. O plano de execução registra:

- `Run_ID`
- `US_ID`
- `Condition`
- `Loop`
- execution order
- date/time
- output path
- status
- error, when applicable

Todas as 120 execuções planejadas foram válidas. O agente foi orientado a atuar
em **modo de auditoria**, considerando apenas a User Story e o contexto fornecido
para a condição correspondente. O prompt experimental está em
`scripts/clarification-gen/clarify-prompt.txt` e as regras de auditoria em
`.specify/memory/constitution.md`.

---

## Ambiente de execução

O ambiente técnico foi registrado no pacote experimental (veja
[`environment/environment.md`](environment/environment.md)).

| Component | Version/configuration |
| --- | --- |
| Date | `2026-07-08T15:07:57-03:00` |
| Operating system | Microsoft Windows 11 Pro, 64 bits |
| PowerShell | `5.1.26100.8457` |
| Spec Kit / specify | `0.12.8.dev0` |
| Codex CLI | `0.143.0` |
| Python | `3.7.9` |
| uv | `0.11.16` |
| Git | `2.48.1.windows.1` |

O ambiente **foi registrado**. A limitação correta é que a reexecução exata pode
depender de componentes externos, como disponibilidade do modelo, comportamento
do serviço subjacente e possíveis variações estocásticas do agente.

---

## Estrutura do repositório

```text
.
├── data/          # Frozen analysis dataset (fonte autoritativa da análise)
├── notebooks/     # analysis_reproducibility.ipynb (reproduz a análise)
├── results/       # Saídas .csv geradas pelo notebook + planilha mestre
├── runs/          # Saídas, logs e metadados preservados das 120 execuções
├── collected-data/# Artefatos intermediários gerados pelo pipeline de execução
├── materials/     # User Stories auditadas e blocos de contexto
├── baselines/     # spec.md base e checklist de requisitos por User Story
├── datasets/      # Dados originais das User Stories
├── environment/   # Registro do ambiente e comandos de replicação
├── scripts/       # Scripts de execução e processamento (inclui bin/)
├── .specify/      # Configuração do Spec Kit e a constitution do experimento
└── .codex/        # Configuração local do Codex CLI usada no desenvolvimento
```

---

## O pipeline de execução (`scripts/bin`)

A pasta `scripts/bin` contém wrappers de conveniência que executam o pipeline de
coleta e processamento. Há uma versão `.bat` (Windows) e uma `.sh`
(Linux/macOS) para cada etapa. O orquestrador `run-pipeline` executa as cinco
etapas em ordem:

| Etapa | Wrapper (`scripts/bin/`) | Script Python | O que faz | Saída |
| --- | --- | --- | --- | --- |
| 1 | `scaffold-runs` | `clarification-gen/scaffold_runs.py` | Cria as 120 pastas em `runs/` a partir de `baselines/` e `materials/` (copia `spec.md`, `user-story.md` e o `context.md` da condição) | `runs/<Run_ID>/` |
| 2 | *(run)* | `clarification-gen/runner.py` | Invoca `codex exec --model gpt-5.5` com o prompt experimental, em ordem randomizada (seed fixa), e grava `output.md`, `codex-log.txt` e `metadata.txt` por run | `collected-data/execution-table.csv` |
| 3 | `check-outputs` | `check-outputs/check_outputs.py` | Verifica se cada run tem um `output.md` não vazio | `collected-data/outputs-check.csv` |
| 4 | `extract-questions` | `clarification-processing/extract_questions.py` | Extrai as linhas de perguntas de clarificação dos `output.md` | `collected-data/questions_raw.csv` |
| 5 | `build-classification-base` | `clarification-processing/build_classification_base.py` | Monta o template de classificação para a anotação manual | `collected-data/classification_base.csv` |

Para rodar o pipeline completo:

```bash
# Windows
scripts\bin\run-pipeline.bat

# Linux/macOS
scripts/bin/run-pipeline.sh
```

Cada etapa também pode ser executada isoladamente pelo wrapper correspondente
(ex.: `scripts/bin/check-outputs.sh`). É necessária uma autenticação válida do
Codex CLI para a etapa 2; nenhuma credencial está incluída no repositório.

Este pipeline corresponde à **reexecução do experimento** (a coleta). A anotação
pelos dois juízes e a adjudicação ocorrem sobre `classification_base.csv` e
resultam na planilha congelada, descrita adiante. A **reprodução da análise**
(muito mais simples e determinística) é feita pelo notebook, descrita na seção
[Notebook de reprodutibilidade](#notebook-de-reprodutibilidade).

---

## Extração e limpeza das perguntas

As saídas brutas das execuções foram processadas para extrair perguntas de
clarificação. Como o formato de saída podia repetir uma mesma pergunta com e sem
a marca `[NEEDS CLARIFICATION]`, duplicatas diretas dentro da mesma execução
foram removidas antes da anotação.

```text
1,039 extracted question lines
− 441 internal duplicates
= 598 annotated questions
```

---

## Anotação independente

As 598 perguntas foram anotadas independentemente por **dois juízes**. Cada
pergunta recebeu classificação para (os nomes são mantidos em inglês porque
correspondem às colunas da planilha e do notebook):

- `informational gap`
- `contextual category`
- `coverage`
- `functional relevance`
- `evidence`
- `justification`

### Contextual category

`contextual category` identifies the type of information required to answer a clarification question. It does not classify the wording of the question itself, but the kind of contextual knowledge that would be needed to resolve the gap.

| Category | Meaning | Typical clarification target |
|---|---|---|
| `Lexical` | The question asks for the meaning, definition, scope or interpretation of a term used in the User Story or context. | Undefined terms, ambiguous labels, domain vocabulary, meaning of expressions. |
| `Operational` | The question asks about rules, behavior, conditions, limits, exceptions, ordering, permissions, state transitions or expected system actions. | Business rules, validation rules, workflows, edge cases, fallback behavior. |
| `Decisional` | The question asks for a product, scope or design decision among possible alternatives. | Whether a feature is in scope, which option should be chosen, what policy should apply. |
| `Systemic` | The question asks about actors, services, data sources, external systems, inputs, outputs or structural dependencies needed by the feature. | Required fields, integrations, authoritative data sources, roles, system dependencies. |
| `Not associated` | The question does not correspond to a meaningful functional clarification gap or falls outside the analysis scope. | Implementation details outside the requirement, irrelevant assumptions, non-functional noise. |

### Coverage

Indica se a informação solicitada já estava disponível no material fornecido ao
agente:

- `Unanswered`: the information was absent;
- `Partially answered`: the information was partially available;
- `Redundant`: the information was already available in the provided material.

### Functional relevance

Indica a importância funcional da pergunta:

- `Necessary`: the gap is required to define or validate the expected behavior;
- `Useful`: the gap is helpful but not strictly required;
- `Non-pertinent`, if applicable.

Na base final, **não houve** casos finais classificados como `Non-pertinent`.

---

## Normalização dos gaps

A unidade principal de análise não é apenas a pergunta literal, mas o
`normalized gap`. Duas perguntas com redações diferentes podem representar a
mesma lacuna informacional. Exemplo:

```text
What ZIP code formats are valid?
Which ZIP code formats must be accepted?
```

Ambas podem ser normalizadas como:

```text
Accepted ZIP code formats
```

Após a anotação independente, os rótulos livres de `informational gap` foram
mapeados para um `codebook`. A base final contém **64 normalized gaps**. A aba
`Gap_normalization` contém o codebook de normalização.

---

## Concordância entre juízes e adjudicação

A concordância foi calculada apenas para as variáveis fechadas (`contextual
category`, `coverage`, `functional relevance`). Ela **não** foi calculada
diretamente sobre os rótulos livres de `informational gap`, porque esses rótulos
podiam variar semanticamente mesmo quando os juízes se referiam à mesma lacuna.

| Variable | Raw agreement / Cohen's kappa |
| --- | --- |
| `contextual category` | 73.75% / κ = 0.444 |
| `coverage` | 71.24% / κ = 0.411 |
| `functional relevance` | 71.24% / κ = 0.244 |

Além disso:

- **188** = agreement on the three closed variables;
- **121** = rows without need for final adjudication;
- **477** = adjudicated rows.

A necessidade de adjudicação considerou não apenas as três variáveis fechadas,
mas também divergências nos rótulos livres de `informational gap` e decisões de
normalização.

---

## Base congelada de análise (frozen analysis dataset)

A planilha congelada é a fonte oficial da análise estatística. Caminho esperado:

```text
data/base.xlsx
```

O notebook lê essa planilha; se ela não estiver presente, usa automaticamente a
cópia em `results/freezed-results.xlsx`. Abas:

| Aba | Função |
| --- | --- |
| `user_stories` | contains the User Stories used in the study. |
| `materials` | contains the experimental materials and context blocks. |
| `executions` | contains the execution plan and run metadata. |
| `raw_info` | contains extracted question lines and duplicate-control fields. |
| `judge-annotation-1` | contains the independent annotations from judge 1. |
| `judge-annotation-2` | contains the independent annotations from judge 2. |
| `Gap_normalization` | contains the normalized gap codebook. |
| `Adjudication` | contains the final adjudicated analysis table. |
| `Gap_convenience` | contains auxiliary mapping information for gap analysis. |

A aba principal para a análise final é **`Adjudication`**.

---

## Notebook de reprodutibilidade

O notebook principal é:

```text
notebooks/analysis_reproducibility.ipynb
```

Ele reproduz a análise estatística e descritiva do artigo **a partir da planilha
congelada** (não reexecuta o agente de LLM).

### Como rodar

```bash
# 1. Instalar as dependências (versões fixadas; Python 3.7.9)
pip install -r requirements.txt
# alternativa com uv:
# uv pip install -r requirements.txt

# 2. Abrir e executar todas as células
jupyter notebook notebooks/analysis_reproducibility.ipynb

# alternativa não interativa:
# jupyter nbconvert --to notebook --execute --inplace notebooks/analysis_reproducibility.ipynb
```

### O que o notebook faz

- carrega a planilha congelada de análise;
- reconstrói as contagens de extração e limpeza;
- recalcula a concordância entre juízes e o Cohen's kappa;
- reconstrói as métricas por execução;
- calcula as estatísticas descritivas por condição;
- aplica o teste de Friedman;
- aplica testes Wilcoxon pareados;
- aplica a correção de Holm;
- calcula o Kendall's W;
- calcula as correlações rank-biserial;
- reproduz os contrastes de RQ2 entre CT e os contextos isolados;
- gera a matriz de eliminação por categoria;
- gera a tabela de comportamento dos gaps;
- exporta os arquivos CSV para `results/`.

---

## Métricas por execução

O notebook cria a tabela `metrics_by_run`, agrupada por `Run_ID`, `US_ID`,
`Condition` e `Loop`, com as métricas:

- `annotated_questions`
- `distinct_normalized_gaps`
- `necessary_unanswered`
- `redundant_questions`

Arquivo exportado:

```text
results/metrics_by_run.csv
```

---

## Estatísticas descritivas por condição

A métrica principal (`necessary_unanswered`) por condição:

| Condition | Mean | Median | SD | 95% CI | N |
| --- | ---: | ---: | ---: | --- | ---: |
| C0 | 2.90 | 3.00 | 0.79 | [2.55; 3.25] | 20 |
| CL | 2.10 | 2.00 | 1.48 | [1.45; 2.75] | 20 |
| CO | 0.65 | 0.50 | 0.75 | [0.35; 0.95] | 20 |
| CD | 1.75 | 1.50 | 1.29 | [1.20; 2.30] | 20 |
| CS | 1.70 | 1.00 | 1.45 | [1.10; 2.35] | 20 |
| CT | 0.65 | 0.00 | 1.09 | [0.20; 1.15] | 20 |

Arquivo exportado:

```text
results/condition_summary.csv
```

---

## Testes estatísticos

O experimento tem desenho de medidas repetidas. Cada bloco é definido por
`US_ID` e `Loop`, gerando 20 blocos pareados:

```text
4 User Stories × 5 repetitions = 20 blocks
```

O notebook monta uma tabela wide com as condições (C0, CL, CO, CD, CS, CT) como
colunas.

### RQ1

Teste de Friedman sobre as seis condições:

```text
χ²(5) = 57.64
p < 0.001
Kendall's W = 0.576
```

Wilcoxon pareado (C0 vs cada condição contextual), com correção de Holm dentro da
família de RQ1:

| Comparison | Adjusted p-value | Effect |
| --- | ---: | ---: |
| C0 vs CL | 0.0389 | r_rb = -0.637 |
| C0 vs CO | 0.0003 | r_rb = -1.000 |
| C0 vs CD | 0.0012 | r_rb = -1.000 |
| C0 vs CS | 0.0029 | r_rb = -0.856 |
| C0 vs CT | 0.0003 | r_rb = -1.000 |

### RQ2

Contrastes pareados adicionais (CT vs contextos isolados), com correção de Holm
aplicada separadamente dentro da família de RQ2:

| Comparison | Adjusted p-value | Effect |
| --- | ---: | ---: |
| CT vs CL | 0.0014 | r_rb = -1.000 |
| CT vs CO | 1.0000 | r_rb = 0.000 |
| CT vs CD | 0.0014 | r_rb = -1.000 |
| CT vs CS | 0.0014 | r_rb = -1.000 |

Interpretação:

- CT was more effective than CL, CD and CS;
- CT did not differ from CO;
- therefore, the combined context did not produce a detectable additional gain
  over operational context in this dataset.

Arquivos exportados:

```text
results/statistical_tests.csv
results/rq2_ct_vs_isolated_tests.csv
```

---

## Distribuições finais

A partir da aba `Adjudication`:

### Final_Coverage

| Coverage | Count | Percentage |
| --- | ---: | ---: |
| Unanswered | 315 | 52.7% |
| Partially answered | 252 | 42.1% |
| Redundant | 31 | 5.2% |

### Final_Relevance

| Relevance | Count | Percentage |
| --- | ---: | ---: |
| Necessary | 387 | 64.7% |
| Useful | 211 | 35.3% |

### Final_Category

| Category | Count | Percentage |
| --- | ---: | ---: |
| Operational | 367 | 61.4% |
| Decisional | 91 | 15.2% |
| Systemic | 72 | 12.0% |
| Lexical | 68 | 11.4% |

Contagens adicionais:

- `Unanswered + Necessary`: 195
- `CT + Unanswered`: 15
- `CT + Unanswered + Necessary`: 13

Arquivo exportado:

```text
results/final_distributions.csv
```

---

## RQ3: matriz de eliminação por categoria

Compara os gaps observados em C0 com aqueles ausentes nas condições contextuais.
A contagem considera gaps distintos por User Story, não perguntas totais.

| Gap category | CL | CO | CD | CS |
| --- | ---: | ---: | ---: | ---: |
| Lexical | 1 | 0 | 2 | 1 |
| Operational | 1 | 2 | 1 | 1 |
| Decisional | 2 | 2 | 2 | 3 |
| Systemic | 3 | 5 | 2 | 2 |
| Not associated | 0 | 0 | 0 | 0 |

Arquivo exportado:

```text
results/category_elimination_matrix.csv
```

---

## RQ4: comportamento dos gaps

Definições:

- `eliminated`: gap appears in C0 for the same User Story but does not appear in
  the contextual condition.
- `emergent`: gap does not appear in C0 for the same User Story but appears in the
  contextual condition.
- `persistent`: gap appears in C0 and continues to appear in the contextual
  condition, in the target category, and is not redundant.
- `unchanged`: gap appears in C0 and continues to appear, but outside the target
  category, and is not redundant.
- `redundant`: gap appears in C0 and in the contextual condition, but in the
  contextual condition it is classified as `Final_Coverage == "Redundant"`.

Target categories:

- CL → Lexical
- CO → Operational
- CD → Decisional
- CS → Systemic
- CT → all categories

| Condition | Eliminated | Persistent | Emergent | Unchanged | Redundant |
| --- | ---: | ---: | ---: | ---: | ---: |
| CL | 7 | 3 | 13 | 25 | 0 |
| CO | 9 | 14 | 10 | 10 | 2 |
| CD | 7 | 4 | 10 | 23 | 1 |
| CS | 7 | 5 | 14 | 21 | 2 |
| CT | 9 | 21 | 11 | 0 | 5 |

Arquivos exportados:

```text
results/gap_behavior_summary.csv
results/gap_behavior_details.csv
```

---

## Mapa artigo → artefato

Todos os arquivos abaixo são gerados ao rodar o notebook.

| Elemento do artigo | Reproduzido por | Arquivo de saída |
| --- | --- | --- |
| Contagens de extração e limpeza | Notebook, a partir de `raw_info` e `executions` | `results/extraction_summary.csv` |
| Concordância dos juízes e Cohen's kappa | Notebook, a partir das colunas dos juízes | `results/judge_agreement_summary.csv` |
| Necessary unanswered gaps por condição | Notebook, a partir de `Adjudication` | `results/condition_summary.csv` |
| Friedman e Kendall's W | Notebook, a partir das métricas por execução | `results/statistical_tests.csv` |
| Wilcoxon C0 vs contextos | Notebook, a partir da tabela pareada | `results/statistical_tests.csv` |
| CT vs contextos isolados | Notebook, a partir da tabela pareada | `results/rq2_ct_vs_isolated_tests.csv` |
| Matriz de eliminação por categoria | Notebook, a partir dos gaps normalizados | `results/category_elimination_matrix.csv` |
| Tabela de comportamento dos gaps | Notebook, a partir dos gaps normalizados e coverage | `results/gap_behavior_summary.csv` |
| Distribuições finais | Notebook, a partir de `Adjudication` | `results/final_distributions.csv` |

Artefatos de apoio: `results/metrics_by_run.csv` e `results/normality_tests.csv`
(Shapiro–Wilk das diferenças pareadas).
