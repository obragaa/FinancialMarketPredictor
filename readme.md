### Estrutura de Diretórios

```
FinancialMarketPredictor/
│
├── data/
│   └── (diretório para armazenar dados coletados e processados)
│
├── models/
│   └── (diretório para salvar modelos treinados)
│
├── notebooks/
│   └── exploration.ipynb (notebook para exploração de dados e experimentos iniciais)
│
├── src/
│   ├── __init__.py
│   ├── config.py (configurações gerais do projeto, como API keys e parâmetros)
│   ├── data_manager.py (script para coleta e preparação de dados)
│   ├── model.py (definição do modelo de machine learning)
│   ├── predictor.py (classe para realizar previsões usando o modelo treinado)
│   └── interface.py (interface gráfica do usuário)
│
├── tests/
│   ├── __init__.py
│   ├── test_data_manager.py (testes para o gerenciador de dados)
│   ├── test_model.py (testes para o modelo de machine learning)
│   └── test_predictor.py (testes para a funcionalidade de previsão)
│
├── requirements.txt (dependências do projeto)
├── readme.md (documentação do projeto)
└── main.py (script principal que executa a aplicação)
```

### Descrição dos Componentes

- **data/**: Este diretório armazena dados brutos e processados, garantindo que o acesso aos dados seja centralizado e organizado.
- **models/**: Contém os modelos treinados salvos. Isso permite reutilizá-los sem necessidade de re-treino, economizando tempo e recursos computacionais.
- **notebooks/**: Jupyter notebooks são úteis para exploração de dados, análises iniciais e visualizações interativas.
- **src/**: O diretório fonte contém todos os scripts Python essenciais para o projeto:
  - `config.py`: Centraliza configurações, como chaves de API e parâmetros globais.
  - `data_manager.py`: Gerencia a coleta e pré-processamento de dados.
  - `model.py`: Constrói e treina o modelo de machine learning.
  - `predictor.py`: Usa o modelo treinado para fazer previsões em novos dados.
  - `interface.py`: Contém a lógica para a interface gráfica, permitindo interações do usuário com o sistema preditivo.
- **tests/**: Contém testes automatizados para diferentes módulos do projeto, o que é crucial para garantir que as mudanças não quebrem funcionalidades existentes.
- **requirements.txt**: Lista todas as bibliotecas necessárias para executar o projeto, facilitando a configuração de ambientes de desenvolvimento e produção.
- **main.py**: Script de entrada para a aplicação. Inicia a interface gráfica e serve como ponto de interação para operações de previsão.


Esse esquema garante que o projeto seja facilmente expansível, testável e manutenível.

---

# Tickers

O símbolo da ação que você deve inserir depende do mercado e das ações que deseja analisar. Esses símbolos são conhecidos como "tickers" e representam abreviações únicas para as ações listadas nas bolsas de valores. Aqui estão alguns exemplos de símbolos de ações populares em diferentes bolsas de valores ao redor do mundo:

### Estados Unidos
- **AAPL**: Apple Inc.
- **MSFT**: Microsoft Corporation
- **GOOGL**: Alphabet Inc. (Google)
- **AMZN**: Amazon.com Inc.
- **TSLA**: Tesla Inc.
- **FB**: Facebook, Inc. (Agora Meta Platforms, Inc., mas ainda negociada como FB)

### Brasil
- **PETR4**: Petrobras (Petróleo Brasileiro S.A.)
- **VALE3**: Vale S.A.
- **ITUB4**: Itaú Unibanco Holding S.A.
- **ABEV3**: Ambev S.A.

### Europa
- **VOW3.DE**: Volkswagen AG (Negociada na Deutsche Börse)
- **NESN.SW**: Nestlé S.A. (Negociada na SIX Swiss Exchange)
- **SAP.DE**: SAP SE (Negociada na Deutsche Börse)

### Ásia
- **TSM**: Taiwan Semiconductor Manufacturing Company Limited (Negociada na NYSE, mas é uma empresa asiática)
- **9984.T**: SoftBank Group Corp. (Negociada na Tokyo Stock Exchange)
- **BABA**: Alibaba Group Holding Limited (Negociada na NYSE, mas é uma empresa chinesa)

### Como Encontrar Símbolos de Ações
- **Consulte o Site da Bolsa**: Você pode encontrar os símbolos das ações diretamente nos sites das bolsas de valores, como a NYSE, NASDAQ, Bovespa, etc.
- **Ferramentas Financeiras Online**: Plataformas como Google Finance, Yahoo Finance e Bloomberg oferecem pesquisas fáceis de símbolos de ações.
- **Consultores Financeiros ou Corretoras**: Plataformas de corretagem online frequentemente fornecem informações detalhadas sobre as ações, incluindo seus símbolos.

Ao testar ou usar seu sistema, escolha um símbolo de ação que seja relevante para suas necessidades de análise ou interesse em investimento. Se você está desenvolvendo o sistema para fins educacionais ou de teste, escolher empresas bem conhecidas como as listadas acima pode ajudar a obter dados mais consistentes e representativos.