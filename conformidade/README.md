# Bateria de conformidade

Testes que verificam se um agente de IA, usando este Playbook, se comporta como o COP-01 §19 exige. Não faz parte do pacote que vai para os projetos: ao criar um projeto a partir deste repositório, a pasta `conformidade/` pode ser apagada.

## O que tem aqui

| Arquivo | Para quê |
|---|---|
| `cenarios.json` | Os 18 cenários do COP-01 (pedido, preparo, comportamento esperado, checagens automáticas) e 4 pedidos de comparação |
| `projeto-exemplo/` | Um app de condomínio mínimo com duas SPECs (Clientes e Financeiro), usado como cobaia |
| `executar.py` | Monta um projeto descartável por cenário, roda o Claude Code, confere o resultado e gera o relatório |

## Como cada cenário é avaliado

1. **Checagens automáticas:** coisas objetivas, como "o código não foi alterado", "a REQ foi criada na SPEC de Financeiro", "não existe `plan.md`".
2. **Avaliação por um segundo agente:** lê o pedido, o comportamento esperado, a resposta do agente e os arquivos criados, e dá o veredito (passou, parcial, falhou) com o motivo em português simples.

Um cenário só passa se as duas avaliações passarem.

## Como rodar

Pré-requisitos: Claude Code instalado e logado, Python 3 e Git.

```bash
python3 conformidade/executar.py                  # os 18 cenários
python3 conformidade/executar.py T-04 T-07        # só alguns
python3 conformidade/executar.py --comparacao     # mesmos pedidos com e sem Playbook
```

O relatório sai em `conformidade/resultados/<data-hora>/relatorio.md`. A pasta `resultados/` não é versionada.

## Limitações

- O agente testado recebe só ferramentas de arquivo. Sem terminal, ele não roda testes nem Git; os cenários foram escritos para isso.
- Cada rodada consome créditos do plano: cerca de 30 mil tokens novos por cenário e quase 200 mil na inicialização (T-01).
- O avaliador também é um modelo de IA. Um veredito "parcial" merece leitura humana do motivo.
