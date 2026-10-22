"""
=============================================================================
GRIT Team Growth & Work OS - Official 17 Career Roadmaps Catalog
-----------------------------------------------------------------------------
Comprehensive, production-grade curricula for 17 high-impact engineering careers:
01. Data Analyst
02. Data Scientist
03. Data Engineer
04. AI Engineer
05. Machine Learning Engineer
06. AI Tools Specialist / AI Automation
07. Cloud Engineer
08. DevOps Engineer
09. Cybersecurity Engineer
10. Backend Developer
11. Full-Stack Developer
12. Frontend Developer
13. Mobile App Developer
14. Database Engineer
15. Data Platform Engineer
16. Software Engineer
17. Robotics / Computer Engineer
=============================================================================
"""

ROADMAP_CATALOG = {
    "Data Analyst": {
        "id": "01_data_analyst",
        "icon": "📊",
        "category": "Data & Analytics",
        "difficulty": "Beginner to Advanced",
        "duration": "4–8 Months",
        "summary": "Raw data ko clean, analyze aur visualize karke business decisions ke liye useful insights aur executive dashboards nikalna.",
        "phases": {
            "Phase 1: Computer aur Data Basics": [
                "Computer hardware, software aur operating system fundamentals",
                "Files, folders aur file extensions manage karna",
                "CSV, XLSX, JSON aur PDF data file formats",
                "Structured aur unstructured data ka difference",
                "Rows, columns, records aur fields architecture",
                "Text, numbers, dates aur Boolean data types",
                "Data quality, missing values aur duplicate records handling",
                "Revenue, profit, expenses, CAC, LTV jaise business metrics",
                "Business questions ko measurable data queries mein convert karna"
            ],
            "Phase 2: Excel & Advanced Spreadsheets": [
                "Workbook, worksheet, cells, ranges aur formatting",
                "SUM, AVERAGE, MIN, MAX & basic aggregations",
                "COUNT, COUNTA aur COUNTIF calculations",
                "SUMIF aur SUMIFS multi-condition math",
                "IF, AND, OR aur IFERROR logic",
                "Relative aur absolute cell references ($A$1)",
                "Sorting, multi-level filtering & deduplication",
                "Text to Columns, Flash Fill & Delimiters",
                "TRIM, LEFT, RIGHT, MID text cleaning",
                "XLOOKUP aur VLOOKUP dynamic lookups",
                "Conditional Formatting & data visual bars",
                "Pivot Tables, Groupings & Calculated Fields",
                "Charts, line graphs, bar charts & slicers",
                "Data Validation, dropdowns & input controls",
                "Date formulas (DATEDIF, EOMONTH) & percentage growth",
                "Messy real-world spreadsheet audit & cleaning",
                "Monthly business executive report design",
                "Practice Project: Interactive Excel Sales & Revenue Dashboard"
            ],
            "Phase 3: SQL for Data Analytics": [
                "Relational Database, table, row aur column architecture",
                "PostgreSQL / SQLite setup & DB client",
                "CREATE TABLE, data types & INSERT statements",
                "SELECT, column aliases & WHERE filtering",
                "ORDER BY, LIMIT, OFFSET & DISTINCT",
                "AND, OR, NOT & operator precedence",
                "BETWEEN, IN aur LIKE wildcard pattern matching",
                "NULL values handling with COALESCE & IS NULL",
                "Aggregate functions: COUNT, SUM, AVG, MIN, MAX",
                "GROUP BY & multi-column grouping",
                "HAVING clause vs WHERE clause",
                "CASE WHEN conditional columns & bucketing",
                "Primary keys, Foreign keys & schema relations",
                "INNER JOIN & data intersection",
                "LEFT JOIN, RIGHT JOIN & FULL OUTER JOIN",
                "Multiple table joins & join condition optimization",
                "Subqueries in SELECT, FROM & WHERE clauses",
                "Common Table Expressions (CTEs) & readability",
                "Window functions: OVER(), PARTITION BY, ORDER BY",
                "ROW_NUMBER, RANK aur DENSE_RANK ranking",
                "LAG aur LEAD period-over-period comparisons",
                "Running totals & moving window averages",
                "SQL Query optimization & EXPLAIN plan basics",
                "Practice: Customer segmentation & order behavior analysis",
                "Project: SQL-based Retail Sales & Churn Analytics"
            ],
            "Phase 4: Business Statistics & Experimentation": [
                "Fractions, percentages, ratios & proportions",
                "Measures of Central Tendency: Mean, median aur mode",
                "Measures of Dispersion: Range, variance & standard deviation",
                "Outliers detection: IQR & Z-score methodology",
                "Probability basics & conditional probability",
                "Normal distribution, standard normal & bell curves",
                "Sampling methods & population vs sample inference",
                "Correlation vs causation & confounding variables",
                "Hypothesis testing basics (Null vs Alternative hypothesis)",
                "Confidence intervals & p-value interpretation",
                "A/B testing fundamentals & test duration modeling",
                "Practice: Compare two marketing campaigns with statistical rigor"
            ],
            "Phase 5: Python for Analytics": [
                "Python & VS Code installation & environment setup",
                "Variables, data types (int, float, str, bool) & operators",
                "Control flow: If, elif, else logic",
                "Loops: For loops, while loops & range()",
                "Data structures: Lists, tuples, dictionaries & sets",
                "Functions, return values, parameters & docstrings",
                "Modules, imports & standard library (math, datetime)",
                "File handling: Reading & writing CSV and TXT files",
                "Error handling with try, except, finally",
                "List comprehensions & dictionary comprehensions",
                "Jupyter Notebook workflow & Markdown notes",
                "Git & GitHub version control basics",
                "Python debugging & troubleshooting techniques",
                "Practice: Automate daily sales report generation with Python"
            ],
            "Phase 6: Data Wrangling with Pandas & NumPy": [
                "NumPy arrays, array indexing & vectorized math",
                "Pandas Series & DataFrames core anatomy",
                "Importing CSV, Excel & JSON data into DataFrames",
                "Data inspection: .info(), .describe(), .head(), .tail()",
                "Filtering & conditional column selections (.loc, .iloc)",
                "Missing value handling: .isna(), .fillna(), .dropna()",
                "Removing duplicate records & datatype conversions",
                "Text cleaning (.str accessor) & datetime conversions (.dt accessor)",
                "GroupBy aggregations & multi-level aggregations",
                "Merging, joining & concatenating DataFrames",
                "Pivot tables & cross-tabulations in Pandas",
                "Outlier investigation & data quality auditing",
                "Project: End-to-end cleaning of a messy 50,000-row e-commerce dataset"
            ],
            "Phase 7: Visualization & Power BI": [
                "Data visualization principles & visual hierarchy",
                "Matplotlib basics: Bar charts, line charts, scatter plots",
                "Seaborn statistical charts: Boxplots, heatmaps, histograms",
                "Power BI Desktop installation & interface overview",
                "Power Query: Data import, ETL steps & transformation rules",
                "Data Modeling: Relationships, Star Schema & Fact/Dimension tables",
                "DAX Basics: Calculated columns vs Measures",
                "Essential DAX: CALCULATE(), FILTER(), ALL(), RELATED()",
                "Time Intelligence DAX: YTD, MTD, SAMEPERIODLASTYEAR",
                "Slicers, dynamic filters & cross-visual filtering",
                "KPI cards, gauges, line charts & drill-downs",
                "Executive dashboard UX, color harmony & mobile layout",
                "Publishing to Power BI Service & scheduled data refresh",
                "Project: Interactive Executive Sales & Customer Retention Dashboard"
            ],
            "Phase 8: Portfolio, Resume & Job Readiness": [
                "Retail Sales Performance Analysis project documentation",
                "Customer Behavior & Cohort Retention project",
                "HR / Marketing campaign ROI analysis project",
                "Executive Financial & Operational dashboard project",
                "Defining business questions, hypotheses & executive takeaways",
                "Documenting ETL, cleaning & analysis steps in GitHub README",
                "Structuring a standout Data Analyst resume with quantifiable metrics",
                "Top 50 SQL interview questions practice (Joins, Window Functions, GroupBy)",
                "Excel & Business statistics interview prep",
                "Portfolio website / Notion portfolio creation",
                "Behavioral interview practice (STAR method for business impact)",
                "Targeted job applications, LinkedIn networking & mock interviews"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Excel advanced modeling (XLOOKUP, Pivot, SUMIFS), Analytics SQL (Window functions, CTEs, Joins), Business metrics (CAC, LTV, Churn, ROI), EDA with Pandas, Power BI DAX & Star Schema modeling.",
            "free_resources": [
                {"title": "SQLBolt — Interactive SQL Practice", "url": "https://sqlbolt.com/"},
                {"title": "Microsoft Excel Help & Video Learning Hub", "url": "https://support.microsoft.com/excel"},
                {"title": "Pandas Official Getting Started Guide", "url": "https://pandas.pydata.org/docs/getting_started/"},
                {"title": "Microsoft Power BI Guided Learning", "url": "https://learn.microsoft.com/power-bi/"},
                {"title": "Mode Analytics SQL Tutorial for Data Analysis", "url": "https://mode.com/sql-tutorial/"}
            ],
            "capstone_project": "Build an Executive SaaS Revenue & Retention Operations Dashboard with Power BI and SQL, featuring monthly recurring revenue (MRR), cohort retention heatmaps, channel ROI, and an executive PDF briefing report.",
            "practice_tasks": [
                "20 products ki sales spreadsheet banao aur XLOOKUP se supplier data link karo",
                "PostgreSQL me customer & order tables bana kar top 10 highest-spending customers nikaalo",
                "Pandas me messy e-commerce CSV load karke missing values aur duplicates clean karo",
                "Power BI me Star Schema design karke dynamic Date slicer aur KPI cards add karo"
            ],
            "job_checklist": [
                "1 End-to-end SQL analysis project on GitHub with detailed README",
                "1 Power BI interactive dashboard with live web link or PDF demo",
                "1 Python Pandas data cleaning & exploratory analysis notebook",
                "Strong mastery of Window Functions (ROW_NUMBER, RANK, LAG/LEAD)",
                "Resume tailored with quantifiable business metrics (e.g. 'Saved 12 hrs/week', 'Identified $50k revenue leak')"
            ]
        }
    },

    "Data Scientist": {
        "id": "02_data_scientist",
        "icon": "🔬",
        "category": "Data & Analytics",
        "difficulty": "Intermediate to Advanced",
        "duration": "6–12 Months",
        "summary": "Data se hidden patterns discover karna, predictive machine learning models banana, aur scientific experiments se business hypotheses validate karna.",
        "phases": {
            "Phase 1: Programming & Mathematics": [
                "Python setup, virtual environments & modern IDE workflow",
                "Variables, conditionals, loops, functions & reusable code modules",
                "Lists, dictionaries, sets & JSON file serialization",
                "NumPy arrays, linear algebra, vectorization & matrix operations",
                "Pandas DataFrames, indexing, merging & vectorized aggregations",
                "Linear Algebra: Vectors, matrices, dot products & eigenvalues",
                "Multivariate Calculus: Derivatives, partial derivatives & gradients",
                "Probability Theory: Random variables, expected values & Bayes theorem",
                "Distributions: Normal, binomial, Poisson & exponential distributions",
                "Central Limit Theorem, sampling bias & standard error",
                "Practice: Code linear regression gradient descent from scratch in Python"
            ],
            "Phase 2: Data Handling, SQL & Exploratory Analysis": [
                "Advanced SQL: Joins, window functions, CTEs & data extraction",
                "Data cleaning: Missing values, imputation strategies & duplicates",
                "Outlier detection: Z-score, Tukey IQR & Isolation Forests",
                "Exploratory Data Analysis (EDA): Univariate, bivariate & multivariate analysis",
                "Visual EDA: Matplotlib, Seaborn distributions, pairplots & correlation heatmaps",
                "Feature distributions, skewness correction & log transforms",
                "Categorical encoding: One-hot encoding, target encoding & ordinal encoding",
                "Feature scaling: StandardScaler, MinMaxScaler & RobustScaler",
                "Data leakage prevention & temporal splitting rules",
                "Project: In-depth EDA & Anomaly Detection Report on 500k customer transactions"
            ],
            "Phase 3: Machine Learning Fundamentals": [
                "AI vs ML vs Deep Learning core concepts & taxonomy",
                "Supervised vs Unsupervised learning paradigms",
                "Features, labels, target variables & training splits",
                "Train, validation and test split methodology",
                "Linear Regression, Ridge (L2) & Lasso (L1) regularization",
                "Logistic Regression, decision boundaries & odds ratios",
                "Decision Trees, entropy, Gini impurity & pruning",
                "Random Forests & Bagging ensemble mechanics",
                "Gradient Boosting: XGBoost, LightGBM & CatBoost",
                "K-Means Clustering, elbow method & silhouette analysis",
                "Principal Component Analysis (PCA) & dimensionality reduction",
                "Underfitting vs Overfitting & Bias-Variance tradeoff",
                "K-Fold Cross-Validation & Stratified K-Fold",
                "Hyperparameter tuning: GridSearchCV, RandomizedSearchCV & Optuna"
            ],
            "Phase 4: Model Evaluation & Validation Rigor": [
                "Regression metrics: MAE, MSE, RMSE, R² & Adjusted R²",
                "Classification metrics: Accuracy, Precision, Recall & F1-Score",
                "Confusion Matrix analysis, Type I & Type II error costs",
                "ROC Curve, AUC score & PR (Precision-Recall) curves",
                "Handling severe class imbalance: SMOTE, class weights & focal loss",
                "Probability threshold calibration & decision curve analysis",
                "Model explainability: SHAP values & LIME feature attribution",
                "Error analysis & model diagnostics on worst-case predictions",
                "Model comparison benchmark tables & statistical significance",
                "Project: End-to-end Customer Churn Prediction Engine with SHAP explanations"
            ],
            "Phase 5: Advanced Data Science, Time-Series & Deep Learning": [
                "Time-series fundamentals: Trend, seasonality, stationarity & noise",
                "Autocorrelation (ACF/PACF), ARIMA, SARIMAX & Prophet forecasting",
                "Recommendation systems: Collaborative filtering & matrix factorization",
                "NLP fundamentals: Tokenization, TF-IDF, stopwords & lemmatization",
                "Word embeddings: Word2Vec, GloVe & sentence embeddings",
                "Deep learning foundations: Perceptrons, MLP & backpropagation",
                "PyTorch essentials: Tensors, Autograd, Dataset, DataLoader",
                "Building, training & validating a neural network in PyTorch",
                "Experiment tracking with MLflow or Weights & Biases",
                "Model serialization: Pickle, Joblib & ONNX runtime",
                "Deploying ML models with Streamlit or FastAPI endpoints",
                "Monitoring model drift & input distribution shifts"
            ],
            "Phase 6: Portfolio, Research Case Studies & Interviews": [
                "House Price Forecasting with advanced feature engineering",
                "Customer Churn Prediction with real-time risk scoring API",
                "E-Commerce Recommendation System engine",
                "Time-Series Sales Demand Forecasting project",
                "GitHub repository packaging, documentation & clean code conventions",
                "Publishing live web demo apps (Streamlit Cloud / HuggingFace Spaces)",
                "Statistics & Probability interview questions practice",
                "Machine learning algorithms theoretical deep dives (math derivations)",
                "Python & SQL live coding interview challenges",
                "Machine Learning System Design interview frameworks",
                "Business case studies & translating models to revenue impact",
                "Resume review, LinkedIn optimization & mock interviews"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Linear algebra, multivariable calculus, hypothesis testing, EDA with Pandas, Scikit-learn algorithms, XGBoost, PyTorch neural networks, SHAP explainability, MLflow.",
            "free_resources": [
                {"title": "Python 3 Official Tutorial", "url": "https://docs.python.org/3/tutorial/"},
                {"title": "Scikit-Learn Official User Guide & Examples", "url": "https://scikit-learn.org/stable/user_guide.html"},
                {"title": "PyTorch Official 60-Minute Blitz & Tutorials", "url": "https://pytorch.org/tutorials/"},
                {"title": "Khan Academy Statistics & Probability", "url": "https://www.khanacademy.org/math/statistics-probability"},
                {"title": "StatQuest with Josh Starmer (ML Visualized)", "url": "https://statquest.org/"}
            ],
            "capstone_project": "Build an End-to-End Predictive Customer Churn & Lifetime Value Engine with automated data preprocessing, XGBoost/PyTorch models, SHAP explainability dashboard, and FastAPI prediction endpoint.",
            "practice_tasks": [
                "NumPy me matrix multiplication aur vector dot-product calculate karo",
                "Scikit-learn se Random Forest classifier train karke ROC-AUC curve plot karo",
                "Credit card fraud dataset me SMOTE aur class weights use karke precision-recall optimize karo",
                "PyTorch me 3-layer neural network bana kar classification problem solve karo"
            ],
            "job_checklist": [
                "2 Production-grade ML projects on GitHub with interactive demos",
                "Deep understanding of bias-variance tradeoff, regularization, and evaluation metrics",
                "Hands-on experience with PyTorch and Scikit-learn",
                "Strong ability to explain model predictions to non-technical stakeholders using SHAP"
            ]
        }
    },

    "Data Engineer": {
        "id": "03_data_engineer",
        "icon": "🔄",
        "category": "Data & Analytics",
        "difficulty": "Intermediate to Advanced",
        "duration": "6–12 Months",
        "summary": "Different sources se data extract karna, robust ETL/ELT pipelines banana, data warehouses design karna aur big data systems maintain karna.",
        "phases": {
            "Phase 1: Programming & Systems Foundations": [
                "Linux command line, file system navigation & permissions (chmod, chown)",
                "Bash scripting, environment variables & cron jobs",
                "Python for Data Engineering: OOP, modular architecture & packaging",
                "Error handling, structured JSON logging & retry decorators",
                "File formats: CSV, JSON, Parquet, Avro & Snappy compression",
                "Interacting with REST APIs, pagination & rate-limit handling",
                "Git workflows: Branching, PRs, merge conflicts & GitOps basics",
                "Database connectivity: SQLAlchemy, Psycopg2 & connection pools",
                "Practice: Write a Python script to fetch paginated REST API data and store as compressed Parquet"
            ],
            "Phase 2: Relational Databases & Dimensional Modeling": [
                "PostgreSQL architecture, buffer pool & WAL (Write-Ahead Logging)",
                "Schema design, DDL/DML, constraints & primary/foreign keys",
                "Complex SQL: CTEs, window functions & recursive queries",
                "Transactions, ACID guarantees & isolation levels (Read Committed, Serializable)",
                "B-Tree Indexes, Composite indexes & EXPLAIN ANALYZE cost optimization",
                "Database normalization (1NF, 2NF, 3NF) vs denormalization",
                "Dimensional Modeling: Kimball methodology, Fact tables vs Dimension tables",
                "Star Schema vs Snowflake Schema design",
                "Slowly Changing Dimensions (SCD Type 1, Type 2, Type 3)",
                "Surrogate keys, grain definition & conformed dimensions",
                "Practice: Design an e-commerce data warehouse schema using Star Schema & SCD Type 2"
            ],
            "Phase 3: Data Pipelines & ETL/ELT Architecture": [
                "ETL (Extract-Transform-Load) vs ELT (Extract-Load-Transform) paradigms",
                "Extract: APIs, webhooks, relational DBs (CDC) & cloud buckets",
                "Transform: Data validation, schema enforcement & Pydantic models",
                "Load: Bulk inserts, COPY command & staging tables",
                "Batch processing vs real-time streaming considerations",
                "Incremental loading, watermark timestamps & CDC (Change Data Capture)",
                "Idempotency, deduplication & exactly-once processing concepts",
                "Data quality checks, Great Expectations & schema evolution handling",
                "Pipeline failure alerts, dead-letter queues & exponential backoff retries",
                "Project: Automated Python API-to-PostgreSQL incremental pipeline with failure alerting"
            ],
            "Phase 4: Big Data, Distributed Computing & Spark": [
                "Data Lake vs Data Lakehouse vs Data Warehouse (Snowflake, BigQuery, Databricks)",
                "OLTP (Row-oriented) vs OLAP (Columnar storage) engines",
                "Parquet columnar storage, column projection & predicate pushdown",
                "Apache Spark architecture: Driver, Executors, Cluster Manager & Stages",
                "PySpark DataFrames, lazy evaluation & execution DAGs",
                "Transformations (narrow vs wide) & Actions",
                "Spark joins: Broadcast hash joins vs Shuffle hash joins",
                "Partitioning, repartition vs coalesce, and shuffle spill mitigation",
                "Event streaming foundations: Apache Kafka architecture (Brokers, Topics, Partitions)",
                "Kafka producers, consumers, consumer groups & offset management",
                "Practice: Process 10GB dataset with PySpark, optimize partition sizing & join performance"
            ],
            "Phase 5: Workflow Orchestration & Cloud Infrastructure": [
                "Workflow orchestration fundamentals & Directed Acyclic Graphs (DAGs)",
                "Apache Airflow architecture: Webserver, Scheduler, Worker & Metadata DB",
                "Authoring Airflow DAGs: Tasks, BashOperator, PythonOperator & TaskFlow API",
                "Airflow dependencies, scheduling intervals, backfills & catchup",
                "Airflow connections, secrets management & dynamic task mapping",
                "Docker fundamentals: Dockerfile, containers, volumes & Docker Compose",
                "Cloud platforms (AWS/GCP): Object storage (S3/GCS), IAM policies & security",
                "Data transformations with dbt (data build tool): Models, tests & lineage",
                "Infrastructure as Code basics with Terraform",
                "CI/CD automation for data pipelines via GitHub Actions"
            ],
            "Phase 6: End-to-End Capstone Projects & Job Prep": [
                "Automated Multi-API scheduled ETL pipeline with Airflow",
                "Dimensional Cloud Data Warehouse with dbt models and tests",
                "PySpark distributed big data transformation pipeline",
                "Real-time event streaming pipeline using Kafka and Spark Streaming",
                "Data quality, automated testing & pipeline monitoring dashboard",
                "Documenting data lineage diagrams & architecture in GitHub README",
                "SQL for Data Engineers interview coding practice (Window functions, joins)",
                "Python data manipulation & algorithm interview challenges",
                "Data system design: Scaling pipelines, handling data skew & backpressure",
                "Resume preparation with quantifiable pipeline metrics & mock interviews"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Linux, Bash, Python, PostgreSQL, Star Schema & SCD2, Apache Airflow DAGs, PySpark distributed dataframes, Kafka streaming, dbt transformations, Docker.",
            "free_resources": [
                {"title": "Apache Airflow Official Documentation & Tutorials", "url": "https://airflow.apache.org/docs/"},
                {"title": "Apache Spark Official Documentation & Quick Start", "url": "https://spark.apache.org/docs/latest/"},
                {"title": "PostgreSQL Official Manual & Architecture Guide", "url": "https://www.postgresql.org/docs/"},
                {"title": "Docker Getting Started Guide", "url": "https://docs.docker.com/get-started/"},
                {"title": "dbt Official Fundamentals Course & Guides", "url": "https://docs.getdbt.com/"}
            ],
            "capstone_project": "Design an Automated End-to-End ELT Pipeline consuming raw event logs from S3, executing dbt incremental transformations into a dimensional data warehouse, orchestrated by Apache Airflow with automated slack alerting.",
            "practice_tasks": [
                "Linux me Bash script likho jo daily backup zip bana kar timestamp ke sath save kare",
                "PostgreSQL me FactSales aur DimCustomer table bana kar SCD Type 2 maintain karo",
                "Airflow DAG banao jo API se data fetch karke clean kare aur failure hone par retry kare",
                "PySpark me Parquet file read karke group by aggregations perform karo"
            ],
            "job_checklist": [
                "Complete GitHub repository with Airflow DAGs, dbt models, and Docker Compose setup",
                "Architecture diagram showing end-to-end data flow (Ingestion -> Storage -> Transform -> Serving)",
                "Proven mastery of SQL (CTEs, Window Functions, Joins, Indexing)",
                "Solid understanding of idempotency, incremental loads, and distributed compute bottlenecks"
            ]
        }
    },

    "AI Engineer": {
        "id": "04_ai_engineer",
        "icon": "🤖",
        "category": "AI & Machine Learning",
        "difficulty": "Intermediate to Advanced",
        "duration": "8–15 Months",
        "summary": "AI models, foundational LLMs aur APIs ka use karke real-world intelligent, agentic aur RAG-driven production applications banana.",
        "phases": {
            "Phase 1: Modern Python & Async Systems": [
                "Python 3.11+ setup, virtual environments & uv / poetry package management",
                "Object-oriented programming, classes, dataclasses & Pydantic V2 models",
                "Asynchronous programming: AsyncIO, event loops, async/await & concurrency",
                "HTTP protocols, REST APIs, JSON parsing & error handling with httpx/aiohttp",
                "Environment variables, secrets management & .env security",
                "Git version control, feature branches & GitHub collaboration",
                "Writing clean modular code, type annotations & automated pytest tests",
                "Docker basics for containerizing Python AI microservices"
            ],
            "Phase 2: Applied Machine Learning & Mathematics": [
                "Linear Algebra: Vectors, matrices, cosine similarity & dot products",
                "Probability & Statistics: Distributions, confidence intervals & Bayes rule",
                "NumPy arrays, broadcasting & high-performance vector math",
                "Pandas for dataset exploration, cleaning & feature extraction",
                "Supervised learning: Regression, classification & Scikit-learn workflows",
                "Evaluating models: Precision, Recall, F1, ROC-AUC & confusion matrix",
                "Data preprocessing: Scaling, tokenization & text vectorization",
                "Training and saving a classical ML model with Scikit-learn"
            ],
            "Phase 3: Deep Learning, Embeddings & Large Language Models": [
                "Neural networks foundations: Weights, biases, activation functions & loss functions",
                "PyTorch essentials: Tensors, autograd, forward pass & backpropagation",
                "Tokens, context windows, vocabulary & tokenizer mechanics (tiktoken)",
                "Transformer architecture overview: Self-attention, encoders & decoders",
                "Vector embeddings: Semantic similarity, embedding models (OpenAI, HuggingFace)",
                "LLM API integration: Chat completions, temperature, top-p, max_tokens",
                "Structured JSON outputs with Pydantic schemas & function calling",
                "Prompt Engineering: System prompts, few-shot examples, chain-of-thought",
                "Handling model rate limits, streaming responses & latency optimization"
            ],
            "Phase 4: RAG & AI Application Development": [
                "Building production backends with FastAPI: Endpoints, dependency injection, CORS",
                "Document ingestion: PDF, DOCX, Markdown & web scraping",
                "Text chunking strategies: Fixed-size, recursive character, semantic chunking",
                "Vector Databases: ChromaDB, Pinecone, Qdrant & pgvector",
                "Retrieval Augmented Generation (RAG): Dense retrieval, hybrid search (BM25 + vector)",
                "Reranking retrieved passages with cross-encoder models (Cohere Rerank)",
                "Conversational memory, session management & history windowing",
                "Tool Calling: Empowering LLMs to query databases, web search & external APIs",
                "Autonomous agent loops: ReAct pattern, LangGraph state graphs, CrewAI",
                "Project: Full-stack RAG Assistant with PDF upload, hybrid search, and citation sources"
            ],
            "Phase 5: Production Deployment, Evaluation & Safety": [
                "Evaluating AI applications: Ragas metrics (Faithfulness, Answer Relevance, Context Recall)",
                "Detecting & mitigating hallucinations, prompt injection & jailbreaking",
                "Data privacy, PII masking & enterprise AI guardrails (NeMo Guardrails)",
                "Measuring & optimizing inference latency, token usage & API costs",
                "Caching LLM responses with Redis / GPTCache",
                "Containerizing FastAPI AI app with Docker & multi-stage builds",
                "Cloud deployment: AWS ECS, GCP Cloud Run, or Render",
                "Structured logging, tracing (LangSmith / Phoenix) & monitoring",
                "CI/CD deployment pipelines with GitHub Actions"
            ]
        },
        "learning_guide": {
            "what_to_learn": "FastAPI, Pydantic, Vector Embeddings, ChromaDB/Pinecone, RAG Architecture, Hybrid Search, Reranking, Tool Calling, LangGraph agents, Ragas evaluation, Docker.",
            "free_resources": [
                {"title": "OpenAI Official Developer Guides & Cookbooks", "url": "https://platform.openai.com/docs/"},
                {"title": "Hugging Face NLP & Deep Learning Course", "url": "https://huggingface.co/learn/nlp-course/"},
                {"title": "LangChain & LangGraph Official Documentation", "url": "https://python.langchain.com/docs/"},
                {"title": "FastAPI Official Production Documentation", "url": "https://fastapi.tiangolo.com/"},
                {"title": "DeepLearning.AI Short Courses on RAG & Agents", "url": "https://www.deeplearning.ai/"}
            ],
            "capstone_project": "Build an Autonomous Multi-Agent Research & Document Synthesis Engine featuring hybrid RAG search over user documents, automated web search tool calling, hallucination checks, and exportable Markdown briefing reports.",
            "practice_tasks": [
                "FastAPI endpoint banao jo user query lekar OpenAI API se structured Pydantic response return kare",
                "ChromaDB me sample documents embed karke cosine similarity search perform karo",
                "PDF parsing script likho jo text ko chunk kare aur hybrid search se relevant chunks extract kare",
                "ReAct agent banao jo custom calculator aur weather API tools ko call kar sake"
            ],
            "job_checklist": [
                "1 End-to-end RAG application deployed live with vector DB and citation grounding",
                "1 Multi-agent application using tool calling and stateful graph execution",
                "Hands-on benchmark numbers showing latency optimization and RAG evaluation scores",
                "Deep understanding of prompt injection defenses and enterprise guardrails"
            ]
        }
    },

    "Machine Learning Engineer": {
        "id": "05_ml_engineer",
        "icon": "🧠",
        "category": "AI & Machine Learning",
        "difficulty": "Intermediate to Advanced",
        "duration": "6–12 Months",
        "summary": "Machine learning models train, optimize, validate, deploy aur production environment me scale aur monitor karna.",
        "phases": {
            "Phase 1: Programming, Systems & Mathematics": [
                "Python software engineering: OOP, clean architecture, type hinting, packaging",
                "Linux terminal, shell scripting, Git version control & virtual environments",
                "Linear Algebra: Matrices, eigenvectors, SVD, dot products, vector norms",
                "Calculus: Gradients, partial derivatives, chain rule, Hessian matrix",
                "Probability & Statistics: Bayesian probability, distributions, hypothesis testing",
                "NumPy array operations, vectorization & high-performance computing",
                "Pandas DataFrames: Fast ETL, aggregations, memory optimization",
                "SQL for ML: Extracting training datasets, joins, window functions",
                "Data cleaning, exploratory data analysis & statistical distribution checks"
            ],
            "Phase 2: Core Machine Learning & Feature Engineering": [
                "ML problem formulation: Framing business problems as ML objectives",
                "Supervised learning: Linear/Ridge/Lasso regression, Logistic regression",
                "Support Vector Machines (SVM), kernel trick & decision boundaries",
                "Decision trees, Random Forests & bagging ensembles",
                "Gradient Boosting machines: XGBoost, LightGBM & CatBoost internals",
                "Unsupervised learning: K-Means, DBSCAN, Hierarchical clustering",
                "Dimensionality reduction: PCA, t-SNE, UMAP",
                "Feature engineering: Encoding, scaling, binning, interaction features",
                "Feature selection: Mutual information, feature importance, recursive elimination",
                "Cross-validation strategies: K-Fold, TimeSeriesSplit, Stratified K-Fold",
                "Hyperparameter optimization: Bayesian optimization with Optuna"
            ],
            "Phase 3: Model Evaluation, Validation & Explainability": [
                "Regression evaluation: MAE, MSE, RMSE, MAPE, R²",
                "Classification evaluation: Accuracy, Precision, Recall, F1, Log-Loss",
                "ROC-AUC curves, Precision-Recall curves & threshold tuning",
                "Handling severe class imbalance: SMOTE, focal loss, class reweighting",
                "Data leakage detection: Train-test contamination, temporal leakage",
                "Model explainability & interpretability: SHAP values, LIME, partial dependence",
                "Error analysis: Identifying failure modes, confusion matrices, residual plots",
                "Statistical model comparison: McNemar test, paired t-test on CV folds"
            ],
            "Phase 4: Deep Learning & Modern Neural Architectures": [
                "Deep learning foundations: Feedforward networks, activation functions (ReLU, GELU)",
                "Optimization algorithms: SGD, Momentum, Adam, AdamW, learning rate schedulers",
                "PyTorch architecture: Tensors, autograd, custom Modules, Datasets, DataLoaders",
                "Training loops, loss tracking, gradient clipping & early stopping",
                "GPU compute: CUDA setup, mixed precision training (torch.cuda.amp)",
                "Convolutional Neural Networks (CNNs) & computer vision transfer learning",
                "Sequence models, RNNs, LSTMs & Transformer self-attention mechanisms",
                "Model serialization: TorchScript, ONNX export, TensorRT optimization"
            ],
            "Phase 5: Production MLOps, Serving & Monitoring": [
                "Model packaging: Packaging trained models into Docker containers",
                "High-performance model serving with FastAPI, Triton, or TorchServe",
                "Experiment tracking & model registry with MLflow / Weights & Biases",
                "Automated training pipelines: Kubeflow Pipelines / Prefect / Airflow",
                "Unit testing for ML: Data validation tests, model regression tests, input invariant tests",
                "Model deployment: Blue/Green deployments, Canary releases, Shadow testing",
                "Monitoring in production: Data drift (Evidently AI / KS-test), concept drift",
                "Model retraining triggers, performance degradation alerting & CI/CD for ML"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Linear algebra, multivariable calculus, Scikit-learn, XGBoost/LightGBM, PyTorch neural networks, CUDA training, MLflow tracking, ONNX model serving, FastAPI, Data Drift monitoring.",
            "free_resources": [
                {"title": "Scikit-Learn Machine Learning Documentation", "url": "https://scikit-learn.org/stable/"},
                {"title": "PyTorch Official Deep Learning Tutorials", "url": "https://pytorch.org/tutorials/"},
                {"title": "MLflow Official Documentation & Guides", "url": "https://mlflow.org/docs/latest/"},
                {"title": "Full Stack Deep Learning Course", "url": "https://fullstackdeeplearning.com/"},
                {"title": "Evidently AI ML Monitoring Documentation", "url": "https://docs.evidentlyai.com/"}
            ],
            "capstone_project": "Build an Automated Real-Time Fraud Detection Engine with feature store pipelines, XGBoost & PyTorch models, MLflow experiment tracking, Dockerized FastAPI microservice, and Evidently AI drift monitoring.",
            "practice_tasks": [
                "XGBoost model train karke Optuna se hyperparameters tune karo",
                "PyTorch model ko ONNX format me export karke inference latency measure karo",
                "MLflow tracking server setup karke metrics aur artifacts log karo",
                "Evidently AI se baseline data aur current data ke beech drift detect karo"
            ],
            "job_checklist": [
                "Production ML pipeline with automated testing and continuous integration",
                "Deep knowledge of ML algorithms from mathematical intuition to implementation",
                "Experience containerizing and serving models with sub-50ms latency",
                "Clear understanding of data drift, model registry, and retraining strategies"
            ]
        }
    },

    "AI Tools Specialist / AI Automation": {
        "id": "06_ai_tools_automation",
        "icon": "⚡",
        "category": "AI & Machine Learning",
        "difficulty": "Beginner to Intermediate",
        "duration": "3–6 Months",
        "summary": "AI tools, APIs aur automation platforms (n8n, Zapier, Webhooks) se repetitive workflows automate karna aur autonomous AI agents deploy karna.",
        "phases": {
            "Phase 1: Generative AI & Prompt Engineering Fundamentals": [
                "Generative AI landscape: LLMs, multimodal models, speech & image models",
                "How LLMs work: Tokens, probability distributions, context windows, limitations",
                "Prompt Engineering frameworks: Role-Task-Context-Constraints-Output format",
                "Few-shot prompting, system instructions, chain-of-thought & step-by-step thinking",
                "AI-assisted research, summarization, extraction & content synthesis",
                "Fact-checking, hallucination verification & critical evaluation of AI outputs",
                "Spreadsheet automation with AI: Formula generation, data cleaning, automated insights",
                "Data privacy, security settings & enterprise compliance rules in AI tools"
            ],
            "Phase 2: Workflow Automation & Webhooks Basics": [
                "Workflow automation anatomy: Triggers, Actions, Filters & Routers",
                "Connecting apps: Forms, Google Sheets, Airtable, Slack, Email & CRM",
                "Understanding Webhooks: Inbound webhooks, outbound webhooks & payload inspection",
                "Working with JSON data: Keys, nested objects, arrays & mapping fields",
                "REST API fundamentals: GET, POST, Headers, Authorization tokens & Bearer keys",
                "Environment variables & secure API key storage",
                "Error handling in workflows: Retries, fallback branches, timeout handling",
                "Workflow execution logs, debugging failed runs & alert notifications"
            ],
            "Phase 3: Advanced Multi-App Automations & No-Code/Low-Code": [
                "Mastering n8n (Self-hosted & cloud): Nodes, expressions, custom JavaScript functions",
                "Make (Integromat) & Zapier advanced multi-step scenario design",
                "Integrating AI APIs (OpenAI, Anthropic, Gemini) directly into automation pipelines",
                "Enforcing structured JSON outputs from AI for deterministic downstream processing",
                "Document processing: Automated invoice parsing, contract summarization, PDF extraction",
                "Automated classification: Email routing, customer ticket sentiment analysis & priority tagging",
                "Human-in-the-loop: Adding manual approval steps before final execution",
                "Scheduled batch jobs, recurring cron executions & deduplication logic",
                "Cost monitoring & token usage budget optimization"
            ],
            "Phase 4: Autonomous AI Agents, Tool Calling & Safety": [
                "AI Agents vs standard linear workflows: Dynamic planning & decision loops",
                "Tool calling & Function execution: Empowering agents to search DBs, fetch web data",
                "Multi-agent coordination: Researcher agent -> Writer agent -> Reviewer agent",
                "Agent memory, persistent state management & conversation context retention",
                "Security & safety: Defending against prompt injection, malicious input sanitization",
                "Least-privilege API key permissions & avoiding unauthorized tool execution",
                "Validating agent output schemas before committing database changes",
                "Failure recovery: Fallback agents, human escalation & grace degradation"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Advanced Prompt Engineering, Webhooks, REST APIs, JSON parsing, n8n workflow builder, OpenAI API, Structured Outputs, Zapier/Make integrations, AI Agents with tool calling.",
            "free_resources": [
                {"title": "OpenAI API Official Documentation", "url": "https://platform.openai.com/docs/"},
                {"title": "n8n Official Documentation & Academy Courses", "url": "https://docs.n8n.io/"},
                {"title": "Zapier Automation Guides & University", "url": "https://zapier.com/learn"},
                {"title": "Make (Integromat) Academy & Interactive Lessons", "url": "https://academy.make.com/"},
                {"title": "Anthropic Claude Prompt Engineering Guide", "url": "https://docs.anthropic.com/claude/docs/prompt-engineering"}
            ],
            "capstone_project": "Build an Automated AI Customer Operations Pipeline: Webhook captures user support requests, AI classifies urgency and sentiment, extracts key details to Airtable, queries knowledge base, drafts personalized replies, and alerts team on Slack.",
            "practice_tasks": [
                "n8n me webhook trigger banao jo form data receive karke email notification bheje",
                "OpenAI API call karke messy raw feedback text se structured JSON sentiment report generate karo",
                "Google Sheet me nayi row add hote hi automated AI summary generate karke update karne ka flow banao",
                "Multi-step agent workflow design karo jisme researcher aur copywriter agents collaborate karein"
            ],
            "job_checklist": [
                "Live demo portfolio of 3+ automated workflows built with n8n or Make",
                "Demonstrated mastery of webhooks, JSON data mapping, and REST API authentication",
                "Experience building prompt pipelines with structured outputs and error handling",
                "Proven business impact (e.g. 'Automated 15 hours of manual data entry per week')"
            ]
        }
    },

    "Cloud Engineer": {
        "id": "07_cloud_engineer",
        "icon": "☁️",
        "category": "Cloud & DevOps",
        "difficulty": "Beginner to Advanced",
        "duration": "6–9 Months",
        "summary": "Cloud platforms (AWS/Azure/GCP) par scalable infrastructure architect karna, security controls implement karna, aur highly available systems manage karna.",
        "phases": {
            "Phase 1: Systems & Networking Foundations": [
                "Computer architecture, virtualization & hypervisors (Type 1 vs Type 2)",
                "Linux administration: File hierarchy, permissions, users, systemd services",
                "Bash scripting: Variables, loops, conditions, automated backup scripts",
                "Networking fundamentals: OSI model, TCP/IP, IP addressing (IPv4/IPv6)",
                "Subnetting, CIDR notation & public vs private subnets",
                "DNS (Domain Name System) record types (A, CNAME, MX, TXT)",
                "HTTP/HTTPS protocols, SSL/TLS certificates & handshakes",
                "Ports, routing tables, NAT gateways & stateful firewalls",
                "Git version control & SSH key pair authentication"
            ],
            "Phase 2: Core Cloud Architecture & Services": [
                "Cloud computing concepts: On-demand self-service, elasticity, shared responsibility model",
                "Public, private & hybrid cloud architectures (IaaS vs PaaS vs SaaS)",
                "Compute services: Virtual machines (EC2/Compute Engine), instance sizing & pricing",
                "Storage services: Object storage (S3/GCS), block storage (EBS/Persistent Disk), file storage (EFS)",
                "Cloud networking: Virtual Private Cloud (VPC), subnets, route tables, internet gateways",
                "Identity & Access Management (IAM): Users, groups, roles, policies, least privilege",
                "Security groups (stateful) vs Network ACLs (stateless)",
                "Load balancing: Application Load Balancers (ALB), health checks & SSL termination",
                "Auto Scaling Groups: Scaling policies, launch templates & high availability"
            ],
            "Phase 3: Cloud Operations, Databases & Reliability": [
                "Deploying & hardening Linux VMs in a private subnet via bastion host",
                "Managed cloud databases: RDS / Cloud SQL (PostgreSQL, MySQL), multi-AZ deployments",
                "Database backups, automated snapshots & point-in-time recovery",
                "Cloud monitoring & observability: CloudWatch / Cloud Monitoring, metrics, alarms",
                "Centralized log ingestion, log groups & metric filters",
                "Multi-AZ architecture, fault tolerance & failover mechanisms",
                "DNS routing & global traffic distribution (Route 53 / Cloud DNS)",
                "Content Delivery Networks (CDN): CloudFront / Cloud CDN edge caching",
                "Troubleshooting connectivity: ping, traceroute, netstat, curl, telnet"
            ],
            "Phase 4: Infrastructure as Code, Automation & Security": [
                "Python (Boto3) & Bash scripts for cloud automation & resource cleanup",
                "Infrastructure as Code (IaC) principles & declarative architecture",
                "Terraform fundamentals: Providers, resources, variables, outputs & state file",
                "Terraform state management: Remote state locking with S3 and DynamoDB",
                "Writing modular, reusable Terraform modules for VPC & compute infrastructure",
                "Container basics: Docker, container images & running containers on cloud",
                "Secrets management: AWS Secrets Manager / KMS encryption keys",
                "Cloud cost optimization: Reserved instances, savings plans, spot instances, lifecycle policies",
                "Disaster Recovery (DR) strategies: Backup & Restore, Pilot Light, Warm Standby, Multi-Region"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Linux, Bash, TCP/IP & CIDR Subnetting, AWS/GCP Core (EC2, S3, VPC, IAM, RDS), Terraform IaC, CloudWatch monitoring, KMS encryption, Cost Optimization.",
            "free_resources": [
                {"title": "AWS Skill Builder & Free Digital Training", "url": "https://aws.amazon.com/training/"},
                {"title": "Microsoft Learn for Azure Cloud", "url": "https://learn.microsoft.com/training/azure/"},
                {"title": "Google Cloud Skills Boost", "url": "https://www.cloudskillsboost.google/"},
                {"title": "HashiCorp Terraform Official Tutorials", "url": "https://developer.hashicorp.com/terraform/tutorials"},
                {"title": "Learn Linux The Hard Way & Bash Guide", "url": "https://linuxjourney.com/"}
            ],
            "capstone_project": "Architect & Deploy a Highly Available, Secure Multi-Tier Web Architecture using Terraform: Public/private VPC subnets, Auto-Scaling Linux compute instances behind an Application Load Balancer, Multi-AZ RDS PostgreSQL database, and CloudWatch alarm alerting.",
            "practice_tasks": [
                "AWS VPC banao with 2 public subnets, 2 private subnets aur NAT Gateway",
                "EC2 instance launch karke Nginx webserver configure karo aur SSL certificate install karo",
                "Terraform code likho jo automated S3 bucket with versioning aur encryption create kare",
                "CloudWatch alarm setup karo jo CPU utilization > 80% hone par email alert bheje"
            ],
            "job_checklist": [
                "GitHub repository with complete Terraform IaC modules for multi-tier architecture",
                "Hands-on experience with VPC networking, CIDR calculations, and IAM security",
                "Understanding of cloud cost management and disaster recovery tiers",
                "Cloud Certification readiness (e.g. AWS Solutions Architect Associate or GCP Cloud Engineer)"
            ]
        }
    },

    "DevOps Engineer": {
        "id": "08_devops_engineer",
        "icon": "♾️",
        "category": "Cloud & DevOps",
        "difficulty": "Intermediate to Advanced",
        "duration": "6–10 Months",
        "summary": "Software delivery lifecycle automate karna: automated CI/CD pipelines, Docker containerization, Kubernetes orchestration, Infrastructure as Code, aur observability.",
        "phases": {
            "Phase 1: Linux, Git & Scripting Foundations": [
                "Linux OS internals: Kernel, processes, memory management, system calls",
                "Linux server commands, permissions (chmod, chown, SUID) & SSH key hardening",
                "Networking for DevOps: DNS, IP, TCP/UDP, ports, netstat, iptables & curl",
                "Git mastery: Rebasing, interactive rebase, cherry-pick, merge strategies & hooks",
                "GitHub Pull Request workflows, branch protection rules & code reviews",
                "Bash scripting: Shell scripts, parameter expansion, exit codes & cron jobs",
                "Python for DevOps: Automating tasks, API requests & CLI utilities with Click/Typer",
                "Software Development Lifecycle (SDLC) & agile deployment methodologies",
                "Automated software testing overview: Unit, integration & end-to-end testing"
            ],
            "Phase 2: Containerization & CI/CD Pipelines": [
                "Container fundamentals: cgroups, namespaces & container runtime (containerd)",
                "Docker architecture, images, containers, networks & persistent volumes",
                "Writing optimized Dockerfiles: Multi-stage builds, non-root users & layer caching",
                "Docker Compose for multi-container local microservice stacks",
                "Continuous Integration (CI) principles: Automated builds, linting & testing",
                "GitHub Actions: Workflows, jobs, steps, triggers, runners & marketplace actions",
                "Managing CI/CD secrets & environment variables securely",
                "Building and pushing container images to container registries (Docker Hub / GHCR)",
                "Automated testing in pipelines & build artifact management"
            ],
            "Phase 3: Kubernetes Orchestration & Infrastructure as Code": [
                "Kubernetes architecture: Control plane (API Server, etcd, Scheduler) & Worker nodes (kubelet, kube-proxy)",
                "Kubernetes core objects: Pods, ReplicaSets, Deployments & Services (ClusterIP, NodePort, LoadBalancer)",
                "ConfigMaps & Secrets management in Kubernetes",
                "PersistentVolumes (PV), PersistentVolumeClaims (PVC) & StorageClasses",
                "Kubernetes Ingress Controllers & TLS routing with cert-manager",
                "Resource management: Requests, limits, Quality of Service (QoS) & Horizontal Pod Autoscaler (HPA)",
                "Helm Package Manager: Charts, templates, values.yaml & releases",
                "Terraform for cloud infrastructure provisioning & remote state management"
            ],
            "Phase 4: Site Reliability, Observability & Security (DevSecOps)": [
                "Monitoring fundamentals: Metrics, logs, traces (The 3 Pillars of Observability)",
                "Prometheus setup: Metrics scraping, PromQL queries, Alertmanager rules",
                "Grafana visualization: Designing operational dashboards & alert notifications",
                "Centralized logging: FluentBit / Promtail, Loki / Elasticsearch & Logstash",
                "Application security scanning: Dependency check (Trivy, Snyk) & static analysis (SonarQube)",
                "Container image vulnerability scanning in CI/CD pipelines",
                "Zero-downtime deployment strategies: Rolling updates, Blue/Green, Canary releases",
                "Production incident response, runbooks, blameless post-mortems & disaster recovery"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Linux internals, Bash, Docker multi-stage builds, GitHub Actions CI/CD, Kubernetes Deployments/Services/Ingress, Helm charts, Terraform IaC, Prometheus & Grafana, Trivy security scanning.",
            "free_resources": [
                {"title": "Docker Official Documentation & Curriculum", "url": "https://docs.docker.com/"},
                {"title": "Kubernetes Official Interactive Tutorials", "url": "https://kubernetes.io/docs/tutorials/"},
                {"title": "GitHub Actions Official Documentation", "url": "https://docs.github.com/actions"},
                {"title": "Prometheus Monitoring Documentation", "url": "https://prometheus.io/docs/introduction/overview/"},
                {"title": "Grafana Tutorials & Dashboards", "url": "https://grafana.com/tutorials/"}
            ],
            "capstone_project": "Build an Automated GitOps CI/CD Delivery Pipeline: Developer commits code -> GitHub Actions runs tests, lints, scans security with Trivy, builds Docker image -> ArgoCD deploys to a Kubernetes cluster with zero-downtime rolling update, monitored by Prometheus and Grafana.",
            "practice_tasks": [
                "Multi-stage Dockerfile likho jo Go ya Node.js app ka image size 500MB se 25MB kar de",
                "GitHub Actions workflow banao jo pull request par unit test run kare aur build verify kare",
                "Kubernetes deployment YAML banao with HPA (Horizontal Pod Autoscaler) aur liveness/readiness probes",
                "Prometheus aur Grafana dashboard configure karo jo CPU, memory aur HTTP 5xx errors monitor kare"
            ],
            "job_checklist": [
                "Complete GitHub repository with end-to-end CI/CD workflow and Kubernetes manifests",
                "Demonstrated knowledge of container optimization, security scanning, and secret management",
                "Deep understanding of Kubernetes networking, ingress routing, and pod lifecycle",
                "Familiarity with production on-call, incident runbooks, and Prometheus alert rules"
            ]
        }
    },

    "Cybersecurity Engineer": {
        "id": "09_cybersecurity_engineer",
        "icon": "🛡️",
        "category": "Cybersecurity",
        "difficulty": "Beginner to Advanced",
        "duration": "6–12 Months",
        "summary": "Systems, networks aur applications ko cyber threats se protect karna, vulnerabilities audit karna, defensive security implement karna aur incident response handle karna.",
        "phases": {
            "Phase 1: Computer Systems, Networking & Cryptography": [
                "Information Security fundamentals: The CIA Triad (Confidentiality, Integrity, Availability)",
                "Computer architecture, memory layout, CPU registers, stack & heap basics",
                "Operating system security: Windows internals (Registry, Event Logs) & Linux permissions",
                "TCP/IP networking stack deep-dive: Handshakes, packets, frames, ARP, ICMP",
                "Network analysis: Wireshark packet capture, filters & inspecting protocols",
                "DNS, HTTP/HTTPS, SSL/TLS handshake & public key infrastructure (PKI)",
                "Firewalls, routers, NAT, subnetting & network segmentation",
                "Cryptography: Symmetric encryption (AES), Asymmetric encryption (RSA, ECC)",
                "Hashing algorithms (SHA-256), HMAC, salts & password hashing (bcrypt, Argon2)",
                "Security governance frameworks: NIST Cybersecurity Framework, ISO 27001, CIS Controls"
            ],
            "Phase 2: Defensive Security, System Hardening & SIEM": [
                "Endpoint security: Antivirus, EDR (Endpoint Detection & Response), host-based firewalls",
                "Operating system hardening: Disabling unnecessary services, CIS benchmarks",
                "Access control: Least privilege principle, Role-Based Access Control (RBAC)",
                "Patch management lifecycle & vulnerability scanners (Nessus, OpenVAS)",
                "Security Information & Event Management (SIEM) architecture (Splunk / Elastic SIEM)",
                "Log ingestion, log parsing, normalization & correlation rules",
                "Security Operations Center (SOC) workflows: Alert triage, true positive vs false positive",
                "Threat intelligence: MITRE ATT&CK framework, Cyber Kill Chain, IOCs (Indicators of Compromise)",
                "Identity & Access Management: Multi-Factor Authentication (MFA), OAuth 2.0, SAML"
            ],
            "Phase 3: Web Application & Cloud Security": [
                "Web application security architecture: Same-Origin Policy, CORS, Cookies & CSP",
                "OWASP Top 10 vulnerabilities: SQL Injection (SQLi), Cross-Site Scripting (XSS)",
                "CSRF, SSRF, Broken Object Level Authorization (BOLA/IDOR), Security Misconfigurations",
                "Hands-on web security labs: Exploiting & remediating OWASP flaws (PortSwigger Academy)",
                "Secure code review principles & input validation / sanitization",
                "API security testing: Authentication flaws, rate limiting, token expiration",
                "Cloud security basics (AWS/Azure): IAM policy auditing, S3 bucket permissions, CloudTrail logs",
                "Secrets management, credential scanning (GitGuardian) & avoiding hardcoded secrets"
            ],
            "Phase 4: Incident Response, Digital Forensics & Threat Hunting": [
                "Incident Response lifecycle: Preparation, Detection, Containment, Eradication, Recovery, Lessons Learned",
                "Incident triage, severity classification & escalation matrix",
                "Evidence preservation: Chain of custody, volatile memory capture (FTK Imager / Volatility)",
                "Disk forensics: File systems, deleted file recovery, timeline analysis",
                "Network forensics: Detecting beaconing, DNS tunneling & data exfiltration",
                "Malware analysis fundamentals: Static analysis, dynamic analysis in sandboxes",
                "Writing incident response runbooks & executive security incident reports",
                "Tabletop incident simulation exercises (Ransomware attack, data breach)"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Networking (TCP/IP, Wireshark), Linux/Windows hardening, Cryptography (AES, RSA, bcrypt), SIEM & SOC alert triage, OWASP Top 10, PortSwigger Labs, Incident Response lifecycle.",
            "free_resources": [
                {"title": "PortSwigger Web Security Academy (Interactive Free Labs)", "url": "https://portswigger.net/web-security"},
                {"title": "TryHackMe Pre-Security & Defensive Paths", "url": "https://tryhackme.com/"},
                {"title": "OWASP Top Ten Web Application Security Risks", "url": "https://owasp.org/www-project-top-ten/"},
                {"title": "NIST Cybersecurity Framework Documentation", "url": "https://www.nist.gov/cyberframework"},
                {"title": "MITRE ATT&CK Knowledge Base", "url": "https://attack.mitre.org/"}
            ],
            "capstone_project": "Build a Virtual Cybersecurity Home Lab & SOC Dashboard: Set up vulnerable machines, configure Splunk/Elastic SIEM to ingest Sysmon logs, simulate attack scenarios (brute-force, port scan, web exploit), detect alerts with custom correlation rules, and document a formal Incident Response Report.",
            "practice_tasks": [
                "Wireshark me PCAP capture open karke cleartext passwords aur suspicious DNS queries dhundho",
                "PortSwigger Web Security Academy me SQL Injection aur XSS ke beginner labs solve karo",
                "Linux VM me SSH port change karke, password login disable karke SSH key setup karo",
                "Splunk ya ELK me sample auth logs upload karke brute-force attack alert rule likho"
            ],
            "job_checklist": [
                "Home lab documentation with network diagrams and SIEM detection rules on GitHub",
                "Completed PortSwigger Web Security Academy practitioner badges",
                "Deep understanding of networking protocols, packet inspection, and log analysis",
                "Ability to articulate incident response steps following NIST / SANS framework"
            ]
        }
    },

    "Backend Developer": {
        "id": "10_backend_developer",
        "icon": "⚙️",
        "category": "Software Engineering",
        "difficulty": "Beginner to Advanced",
        "duration": "6–9 Months",
        "summary": "High-performance server-side architecture, RESTful/gRPC APIs, database persistence, authentication, caching, aur scalable microservices design karna.",
        "phases": {
            "Phase 1: Programming Language Mastery": [
                "Choose primary language: Python (FastAPI/Django) or JavaScript/TypeScript (Node.js/Express)",
                "Variables, memory model, data types, type hints & strict typing",
                "Control flow, exception handling & defensive programming",
                "Object-Oriented Programming (OOP): Classes, inheritance, polymorphism, encapsulation",
                "Data structures: Arrays, hash maps/dictionaries, stacks, queues, sets",
                "File I/O, streams, buffers & JSON serialization",
                "Asynchronous programming: Event loop, Promises / AsyncIO, non-blocking I/O",
                "Git version control, feature branches, pull requests & code review standards"
            ],
            "Phase 2: Web Protocols & RESTful API Design": [
                "Client-Server architecture, Request-Response cycle, statelessness",
                "HTTP protocols (HTTP/1.1, HTTP/2), HTTPS & TLS encryption",
                "HTTP methods: GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD",
                "HTTP status codes: 2xx (Success), 3xx (Redirect), 4xx (Client error), 5xx (Server error)",
                "RESTful API design principles: Resource naming, pagination, filtering, sorting",
                "Request validation, schema validation with Pydantic or Zod",
                "Middleware architecture: Logging, CORS headers, rate limiting, request timing",
                "API documentation with OpenAPI / Swagger specifications"
            ],
            "Phase 3: Backend Framework & Security Architecture": [
                "Structuring scalable backend projects: Controller-Service-Repository pattern",
                "Environment configuration, secrets management & config loaders",
                "Authentication systems: Session-based auth vs Token-based auth (JWT)",
                "Password hashing algorithms (bcrypt, Argon2) & secure salt generation",
                "Role-Based Access Control (RBAC) & authorization guards",
                "HTTP-Only secure cookies, token refresh rotation & revocation lists",
                "Security defenses: SQL injection prevention, XSS sanitization, CORS configuration",
                "Error handling: Centralized exception handlers & consistent JSON error schemas"
            ],
            "Phase 4: Databases, ORMs & Query Optimization": [
                "Relational databases: PostgreSQL / SQLite deep-dive",
                "Schema modeling: Tables, datatypes, primary keys, foreign keys & relationships",
                "Writing clean SQL queries: Joins, aggregations, CTEs, window functions",
                "ORMs vs Query Builders (SQLAlchemy, Prisma, Drizzle) - Pros and Cons",
                "Database migrations: Alembic / Prisma migrate, version-controlled schemas",
                "Transactions, ACID properties, isolation levels & deadlock avoidance",
                "Indexing strategies: B-Tree indexes, composite indexes, query execution plans (EXPLAIN)",
                "Connection pooling & optimizing database connection limits"
            ],
            "Phase 5: Production Engineering, Caching & Scalability": [
                "In-Memory Caching with Redis: Cache-Aside pattern, TTL expiration, invalidation",
                "Rate limiting algorithms: Token Bucket, Leaky Bucket, Sliding Window",
                "Asynchronous background workers & task queues (Celery, BullMQ)",
                "Automated testing: Unit tests, integration tests & API tests (Pytest / Jest)",
                "Containerizing backend services with multi-stage Dockerfiles",
                "Cloud deployment: Docker containers on AWS ECS, Cloud Run, or Render",
                "Structured logging, health check endpoints (/healthz) & Prometheus metrics",
                "System design basics: Load balancing, horizontal scaling, database read replicas"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Python/FastAPI or Node.js/Express, RESTful standards, PostgreSQL schema design & migrations, JWT auth, Redis caching, Pytest automated testing, Docker containerization.",
            "free_resources": [
                {"title": "FastAPI Official Documentation & Tutorial", "url": "https://fastapi.tiangolo.com/"},
                {"title": "Node.js Official Learning Guide", "url": "https://nodejs.org/en/learn"},
                {"title": "PostgreSQL Official Documentation", "url": "https://www.postgresql.org/docs/"},
                {"title": "Redis Official Guides & Data Types", "url": "https://redis.io/docs/"},
                {"title": "ByteByteGo System Design Basics", "url": "https://bytebytego.com/"}
            ],
            "capstone_project": "Build a Production-Ready Multi-Tenant REST API Backend featuring JWT auth with refresh token rotation, PostgreSQL database with migrations, Redis caching, Celery background worker queue for emails, automated Pytest test suite, and Docker deployment.",
            "practice_tasks": [
                "FastAPI ya Express me full CRUD API banao with input validation and custom error responses",
                "JWT authentication system build karo with password hashing, login, and protected routes",
                "PostgreSQL me complex JOIN query likho aur EXPLAIN ANALYZE se execution cost compare karo",
                "Redis cache implement karo jo slow database query results ko 60 seconds ke liye cache kare"
            ],
            "job_checklist": [
                "Clean GitHub repository with clear architectural layering (Router -> Service -> DB)",
                "High automated test coverage with Pytest or Jest (>80% coverage)",
                "Live deployed API on cloud with interactive Swagger/OpenAPI documentation",
                "Strong mastery of SQL, indexing, database relations, and caching tradeoffs"
            ]
        }
    },

    "Full-Stack Developer": {
        "id": "11_fullstack_developer",
        "icon": "🌐",
        "category": "Web & Frontend",
        "difficulty": "Beginner to Advanced",
        "duration": "8–12 Months",
        "summary": "Modern interactive frontend, robust backend APIs, database persistence, aur cloud deployment ko seamlessly integrate karke complete web applications banana.",
        "phases": {
            "Phase 1: Web Foundations & Modern JavaScript": [
                "Semantic HTML5 document structure, accessibility (ARIA) & SEO meta tags",
                "Modern CSS: Box model, Flexbox layout, CSS Grid, media queries & responsive design",
                "CSS variables (design tokens), animations & smooth user transitions",
                "JavaScript fundamentals: Data types, loops, functions, arrow functions, scope",
                "DOM manipulation, event listeners, bubbling, delegation & form handling",
                "Modern ES6+: Destructuring, spread/rest, template literals, modules (import/export)",
                "Asynchronous JavaScript: Promises, async/await, Fetch API & error handling",
                "Git & GitHub: Repositories, commits, branching, merging & pull requests"
            ],
            "Phase 2: Modern Frontend Frameworks (React)": [
                "React architecture: Component-based UI, JSX syntax & Virtual DOM",
                "Props, State & unidirectional data flow",
                "React Hooks: useState, useEffect, useRef, useMemo, useCallback",
                "Component lifecycle & handling side effects cleanly",
                "State management: Context API, Zustand or Redux Toolkit",
                "Client-side routing with React Router / TanStack Router",
                "Forms & validation with React Hook Form & Zod schema validation",
                "Building responsive, reusable component libraries with Tailwind CSS or Vanilla CSS",
                "Handling loading states, empty states, error boundaries & toast notifications"
            ],
            "Phase 3: Backend API Engineering": [
                "Server runtime: Node.js/Express or Python/FastAPI",
                "RESTful API architecture: Routes, controllers, middleware & services",
                "Request validation, status codes & structured error responses",
                "Authentication systems: JWT, HTTP-Only cookies, bcrypt password hashing",
                "Protected routes, role-based authorization & session expiration",
                "File upload handling (Multer, cloud object storage S3/Cloudinary)",
                "API testing with Postman / Bruno & automated endpoint tests"
            ],
            "Phase 4: Database Integration & Full-Stack Sync": [
                "Relational databases (PostgreSQL) vs NoSQL (MongoDB)",
                "Database design: Schemas, tables, relations (1-to-1, 1-to-many, many-to-many)",
                "ORMs / Query builders: Prisma, Drizzle, SQLAlchemy",
                "Database migrations & version-controlled schema evolution",
                "Connecting React frontend to Backend APIs with Axios / TanStack Query (React Query)",
                "Server-side data caching, refetching, optimistic UI updates",
                "Real-time communication with WebSockets / Socket.io"
            ],
            "Phase 5: Production Deployment & Meta-Frameworks": [
                "Next.js App Router: Server Components (RSC), Client Components, Server Actions",
                "Server-Side Rendering (SSR) vs Static Site Generation (SSG) vs Client-Side (CSR)",
                "Environment variables management (.env.local, .env.production)",
                "Docker basics for containerizing full-stack applications",
                "Deploying frontend (Vercel/Netlify) and backend/database (Render/Supabase/Railway)",
                "Performance optimization: Code splitting, lazy loading, image optimization (next/image)",
                "Web vitals audits (LCP, INP, CLS) with Chrome DevTools"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Semantic HTML, Modern CSS, ES6+ JS, React Components & Hooks, Next.js App Router, Node.js/FastAPI backend, PostgreSQL with Prisma/SQLAlchemy, TanStack Query, Vercel/Render deployment.",
            "free_resources": [
                {"title": "MDN Web Docs (The Web Development Bible)", "url": "https://developer.mozilla.org/"},
                {"title": "React.dev Official Documentation & Interactive Tutorial", "url": "https://react.dev/learn"},
                {"title": "Next.js Official Learn Course", "url": "https://nextjs.org/learn"},
                {"title": "The Modern JavaScript Tutorial (javascript.info)", "url": "https://javascript.info/"},
                {"title": "Prisma ORM Official Documentation", "url": "https://www.prisma.io/docs"}
            ],
            "capstone_project": "Build a Full-Stack Collaborative Project & Sprint Management Workspace: Next.js frontend with drag-and-drop Kanban boards, real-time WebSocket task status updates, JWT authentication, PostgreSQL database with Prisma, and full deployment on Vercel and Supabase.",
            "practice_tasks": [
                "Pure HTML/CSS se responsive pricing table component banao with hover animations",
                "React me interactive Todo app banao with local storage persistence and custom hooks",
                "Full-stack auth flow build karo: Register, Login, JWT cookie, and protected user profile page",
                "TanStack Query use karke backend API data fetch karo with optimistic UI deletion"
            ],
            "job_checklist": [
                "2 Full-stack web applications deployed live with source code on GitHub",
                "Responsive on mobile, tablet, and desktop viewports with zero layout breakage",
                "Secure authentication and data validation on both frontend and backend",
                "Clean README with architecture diagram, environment setup instructions, and demo link"
            ]
        }
    },

    "Frontend Developer": {
        "id": "12_frontend_developer",
        "icon": "🎨",
        "category": "Web & Frontend",
        "difficulty": "Beginner to Advanced",
        "duration": "4–8 Months",
        "summary": "High-performance, accessible, visually stunning aur responsive user interfaces design aur develop karna using modern HTML5, CSS3, JavaScript/TypeScript, aur React.",
        "phases": {
            "Phase 1: HTML5 & Semantic Web Architecture": [
                "HTML document structure, DOCTYPE, head, meta tags & character encodings",
                "Semantic elements: header, nav, main, section, article, aside, footer",
                "Accessible headings hierarchy (single h1 rule, h2-h6 nesting)",
                "Links, buttons, images (srcset, sizes, loading='lazy') & figure/figcaption",
                "Forms architecture: input types, labels, fieldset, legend, validation attributes",
                "Accessibility (a11y) essentials: ARIA landmarks, roles, aria-labels & screen readers",
                "SEO fundamentals: Page title tags, meta descriptions, OpenGraph tags",
                "Browser DevTools: DOM inspection, modifying elements & debugging"
            ],
            "Phase 2: Modern CSS3, Layouts & Animations": [
                "CSS syntax, selectors, specificity calculation & the Cascade",
                "Box model: Content, padding, border, margin, box-sizing: border-box",
                "Colors: HSL, RGB, HEX, opacity & modern color systems",
                "Typography: Google Fonts, web-safe fonts, font-display, fluid typography",
                "Flexbox layout: Direction, wrap, justify-content, align-items, flex-grow/shrink",
                "CSS Grid: Grid template columns/rows, gap, auto-fit, minmax(), areas",
                "CSS Positioning: Static, relative, absolute, fixed, sticky & z-index stacking",
                "Media queries & mobile-first responsive design strategies",
                "CSS Custom Properties (CSS variables) & theming (Light/Dark mode)",
                "Transitions, keyframe animations, cubic-bezier timing & micro-interactions"
            ],
            "Phase 3: JavaScript Programming & DOM": [
                "JS syntax, variables (let, const), data types, operators & coercion",
                "Conditionals, loops (for, for...of, for...in) & error handling (try/catch)",
                "Functions, arrow functions, default parameters, closures & scope",
                "Arrays & array methods: map, filter, reduce, find, some, every, sort",
                "Objects: Methods, destructuring, optional chaining (?.), nullish coalescing (??)",
                "DOM manipulation: querySelector, classList, innerHTML, createElement, append",
                "DOM Events: click, input, submit, change, keydown, event delegation",
                "Asynchronous JS: Event loop, callback queue, Promises, async/await",
                "Fetch API: Consuming REST APIs, headers, JSON parsing, error states"
            ],
            "Phase 4: Modern React & TypeScript": [
                "Package management: npm / pnpm / yarn & Vite project initialization",
                "TypeScript for Frontend: Types, interfaces, generics, type-safe props",
                "React components, JSX rules, props & component composition",
                "State management with useState and handling complex state objects",
                "Side effects with useEffect, cleanup functions & dependency arrays",
                "Custom hooks creation for reusable logic (e.g., useDebounce, useLocalStorage)",
                "Performance hooks: useMemo, useCallback, React.memo",
                "Client-side routing with React Router / TanStack Router",
                "Component libraries & styling solutions (Tailwind CSS, CSS Modules, Styled Components)"
            ],
            "Phase 5: Professional Engineering, Performance & Testing": [
                "State management for large apps: Zustand, Jotai or Redux Toolkit",
                "Server state management with TanStack Query (React Query)",
                "Form libraries: React Hook Form & Zod schema validation",
                "Web Performance optimization: Code splitting (React.lazy), tree shaking, bundle analysis",
                "Core Web Vitals: Largest Contentful Paint (LCP), Interaction to Next Paint (INP), CLS",
                "Automated testing: Unit testing components with Vitest & React Testing Library",
                "Cross-browser testing, responsive testing & keyboard navigation auditing",
                "Building, deploying & continuous delivery on Vercel / Netlify / Cloudflare Pages"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Semantic HTML5, CSS Flexbox & Grid, CSS Custom Properties, Modern ES6+ JS, TypeScript, React Components & Hooks, TanStack Query, Core Web Vitals optimization.",
            "free_resources": [
                {"title": "MDN Web Docs — Front-End Developer Path", "url": "https://developer.mozilla.org/"},
                {"title": "React.dev Official Documentation", "url": "https://react.dev/"},
                {"title": "TypeScript Official Handbook for Developers", "url": "https://www.typescriptlang.org/docs/"},
                {"title": "Web.dev by Google — Learn CSS & Core Web Vitals", "url": "https://web.dev/learn/css/"},
                {"title": "Modern CSS Solutions by Stephanie Eckles", "url": "https://moderncss.dev/"}
            ],
            "capstone_project": "Build an Ultra-Premium Cyberpunk Glassmorphic Analytics Dashboard: Interactive Plotly/Chart.js graphs, real-time cryptocurrency/stock price ticker via WebSocket, theme switcher (Dark Cyber/Light), keyboard accessibility, and a 100/100 Lighthouse performance score.",
            "practice_tasks": [
                "Semantic HTML aur pure CSS se 100% accessible multi-step form build karo",
                "Flexbox aur Grid combine karke dynamic responsive e-commerce product catalog banao",
                "TypeScript me type-safe custom hook `useFetch` likho with loading, error aur data states",
                "React me virtualized list implement karo jo 10,000 items ko smoothly render kare"
            ],
            "job_checklist": [
                "Portfolio website showcasing 3 responsive, interactive React/TypeScript web apps",
                "Demonstrated 90+ score on Google Lighthouse for Performance, Accessibility, Best Practices, SEO",
                "Clean GitHub repositories with well-structured component architecture",
                "Strong ability to convert Figma UI designs into pixel-perfect responsive code"
            ]
        }
    },

    "Mobile App Developer": {
        "id": "13_mobile_developer",
        "icon": "📱",
        "category": "Mobile Engineering",
        "difficulty": "Beginner to Intermediate",
        "duration": "6–10 Months",
        "summary": "Cross-platform (Flutter / React Native) ya Native (Kotlin/Swift) technologies se responsive, fast aur offline-first mobile applications build aur publish karna.",
        "phases": {
            "Phase 1: Programming Foundations & Mobile Concepts": [
                "Choose technology stack: Cross-Platform (Flutter with Dart) or (React Native with TypeScript)",
                "Programming fundamentals: Variables, control flow, functions, OOP, collections",
                "Asynchronous programming: Async/await, Futures, Streams, Event loop",
                "Mobile operating systems architecture: Android runtime (ART) vs iOS Darwin kernel",
                "Mobile application lifecycle: Active, Paused, Resumed, Inactive, Background, Terminated",
                "Mobile UI design principles: Touch targets, thumb zones, safe areas, navigation bars",
                "Development environment setup: Android Studio, Xcode (for Mac), SDK managers, emulators"
            ],
            "Phase 2: UI Building & State Management": [
                "Widget/Component tree architecture: Stateless vs Stateful components",
                "Layouts: Columns, Rows, Stacks, Containers, Flex, Expanded, Padding",
                "Scrollable views: ListView, GridView, CustomScrollView, slivers",
                "Design systems: Material Design 3 (Android) & Cupertino (iOS) standards",
                "Handling user input: Text fields, buttons, gestures, sliders, dropdowns",
                "Navigation & routing: Stack-based navigation, deep linking, tab bars, drawer menus",
                "State management architecture: Riverpod / Bloc / Provider (Flutter) OR Zustand / Redux (React Native)",
                "Light mode and Dark mode adaptive theming"
            ],
            "Phase 3: Networking, Local Storage & Hardware APIs": [
                "HTTP networking: REST APIs, JSON serialization & deserialization",
                "Handling network states: Loading spinners, error states, pull-to-refresh",
                "Local persistence: SQLite (sqflite), Hive, SharedPreferences / AsyncStorage",
                "Offline-first architecture: Caching remote data locally and synchronizing when online",
                "Device permissions: Camera, photo library, microphone, location services",
                "Geolocation & Maps integration (Google Maps / Mapbox)",
                "Push Notifications: Firebase Cloud Messaging (FCM) setup & local notifications",
                "Biometric authentication: Fingerprint / Face ID login integration"
            ],
            "Phase 4: Testing, Performance & App Store Publishing": [
                "Unit testing business logic & state management stores",
                "Widget / Component UI testing & user interaction automation",
                "Performance profiling: Avoiding jank, 60fps/120fps rendering, memory leaks, image caching",
                "Battery & network bandwidth optimization",
                "App signing: Keystore generation (Android) & Provisioning Profiles / Certificates (iOS)",
                "Building release binaries: Android App Bundle (.aab) & iOS Archive (.ipa)",
                "Google Play Console: Store listing, privacy policy, screenshots, releases",
                "Apple App Store Connect: App review guidelines, TestFlight beta testing, app review submission"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Dart & Flutter (or TypeScript & React Native), Widget Tree, State Management (Riverpod/Bloc), Offline SQLite/Hive caching, REST APIs, FCM Push Notifications, Play Store / App Store release pipeline.",
            "free_resources": [
                {"title": "Flutter Official Documentation & Codelabs", "url": "https://docs.flutter.dev/"},
                {"title": "Dart Language Tour & Interactive Sandbox", "url": "https://dart.dev/guides/language/language-tour"},
                {"title": "React Native Official Getting Started Guides", "url": "https://reactnative.dev/docs/getting-started"},
                {"title": "Android Developers Official Training Courses", "url": "https://developer.android.com/courses"},
                {"title": "Apple Developer Documentation & Swift Guides", "url": "https://developer.apple.com/"}
            ],
            "capstone_project": "Build a Cross-Platform Mobile Personal Productivity & Habit Tracker App: Adaptive Dark Cyber UI, local SQLite offline caching with auto cloud sync, biometric Face ID login, push notification reminders, and interactive progress charts.",
            "practice_tasks": [
                "Flutter ya React Native me custom UI card banao with smooth touch ripple animation",
                "REST API se news feed load karo with infinite scrolling pagination and pull-to-refresh",
                "SQLite me offline notes store karo jisme user add, edit aur delete kar sake bina internet ke",
                "Biometric authentication integrate karo jo device ke fingerprint scanner se login allow kare"
            ],
            "job_checklist": [
                "1 Complete mobile app published on Google Play Store or TestFlight (or working .apk demo)",
                "Clean repository on GitHub showcasing state management and clean architecture",
                "Working demo video highlighting offline mode, push notifications, and animations",
                "Clear understanding of app signing, permissions, and app review submission guidelines"
            ]
        }
    },

    "Database Engineer": {
        "id": "14_database_engineer",
        "icon": "🗄️",
        "category": "Data & Analytics",
        "difficulty": "Beginner to Advanced",
        "duration": "6–8 Months",
        "summary": "Relational aur distributed databases ko reliable, secure, high-throughput aur query-optimized banana.",
        "phases": {
            "Phase 1: Database Architecture & Advanced SQL": [
                "Relational model fundamentals, relational algebra, tuple calculus",
                "Database engine architecture: Storage engine, Buffer pool, Query planner, Execution engine",
                "SQL DDL, DML, DCL, TCL commands & constraints",
                "Complex SQL queries: Filtering, grouping, multiple joins, subqueries",
                "Window functions: ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD",
                "Common Table Expressions (CTEs), recursive CTEs & hierarchical data modeling",
                "Null handling, coalesce, nullif, three-valued logic (TRUE, FALSE, UNKNOWN)",
                "Views, Materialized Views & automated refresh strategies"
            ],
            "Phase 2: Relational Schema Design & Data Integrity": [
                "Entity Relationship (ER) diagramming: Entities, attributes, cardinalities",
                "Relationship types: One-to-One, One-to-Many, Many-to-Many with junction tables",
                "Database normalization: 1NF, 2NF, 3NF, BCNF & eliminating data anomalies",
                "Controlled denormalization: Performance tradeoffs & read-heavy optimization",
                "Transactions & ACID guarantees: Atomicity, Consistency, Isolation, Durability",
                "Transaction Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable",
                "Concurrency phenomena: Dirty reads, non-repeatable reads, phantom reads, serialization anomalies",
                "Schema migration tools: Version-controlled schema changes & zero-downtime migrations"
            ],
            "Phase 3: Indexing Strategies & Query Optimization": [
                "Index data structures: B-Tree, B+ Tree, Hash indexes, GIN, GiST, BRIN indexes",
                "Index types: Clustered vs non-clustered, composite indexes, covering indexes, partial indexes",
                "Analyzing query execution plans: EXPLAIN, EXPLAIN ANALYZE, cost estimation",
                "Optimizing slow queries: Eliminating full table scans, SARGable predicates, join ordering",
                "Table partitioning strategies: Range partitioning, List partitioning, Hash partitioning",
                "Locks & Concurrency control: Shared locks, exclusive locks, row-level locks, table locks",
                "Deadlocks: Detection, resolution, lock timeouts & transaction retry strategies",
                "Connection pooling: PgBouncer, sizing connection pools & memory allocation"
            ],
            "Phase 4: High Availability, Replication, Security & Disaster Recovery": [
                "Database security: User roles, permissions, least-privilege access, row-level security (RLS)",
                "Data encryption: Encryption at rest (TDE), encryption in transit (TLS), column-level encryption",
                "Database backup strategies: Logical backups (pg_dump), Physical backups (base backups)",
                "Point-In-Time Recovery (PITR) using Write-Ahead Logs (WAL archiving)",
                "Database replication: Master-Slave, synchronous vs asynchronous replication, read replicas",
                "High availability & automated failover (Patroni, Keepalived)",
                "Database health monitoring: Query latency, buffer cache hit ratio, bloat, autovacuum tuning",
                "Disaster recovery planning, RTO (Recovery Time Objective) & RPO (Recovery Point Objective)"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Relational Algebra, 3NF/BCNF normalization, ACID & Isolation levels, B-Tree index mechanics, EXPLAIN ANALYZE query tuning, Table Partitioning, WAL archiving & PITR, Replication.",
            "free_resources": [
                {"title": "PostgreSQL Official Documentation & Manual", "url": "https://www.postgresql.org/docs/"},
                {"title": "Use The Index, Luke! Database Indexing Guide", "url": "https://use-the-index-luke.com/"},
                {"title": "Database Internals Book Resources (Alex Petrov)", "url": "https://www.databass.dev/"},
                {"title": "MySQL Official Reference Manual", "url": "https://dev.mysql.com/doc/"},
                {"title": "SQLite WAL Mode & Architecture Guide", "url": "https://www.sqlite.org/wal.html"}
            ],
            "capstone_project": "Design a High-Throughput Financial Ledger Database: 3NF relational schema with strict check constraints, multi-tenant isolation, composite B-Tree indexes optimizing queries to <5ms, EXPLAIN-validated query plans, automated partition pruning, and WAL-based point-in-time recovery demo.",
            "practice_tasks": [
                "10 million rows wali table create karke slow unindexed query aur indexed query ka execution plan compare karo",
                "PostgreSQL me Range Partitioning setup karo jo logs table ko month-wise partition kare",
                "Deadlock scenario reproduce karo do transactions ke beech aur lock resolution verify karo",
                "PostgreSQL me WAL archiving enable karke specific timestamp par Point-In-Time Recovery perform karo"
            ],
            "job_checklist": [
                "GitHub repository with documented schema design, migration scripts, and indexing benchmarks",
                "Proven ability to read and optimize complex EXPLAIN ANALYZE execution plans",
                "Deep conceptual mastery of ACID, isolation levels, and lock contention",
                "Hands-on experience configuring backups, WAL archiving, and replication"
            ]
        }
    },

    "Data Platform Engineer": {
        "id": "15_data_platform_engineer",
        "icon": "🏗️",
        "category": "Data & Analytics",
        "difficulty": "Intermediate to Advanced",
        "duration": "8–12 Months",
        "summary": "Enterprise data teams ke liye scalable data platform infrastructure, distributed processing engines, reusable data pipelines, aur governance platforms build karna.",
        "phases": {
            "Phase 1: Systems, Distributed Compute & Platform Foundations": [
                "Advanced Python for data systems: Concurrency, generators, memory optimization",
                "Advanced SQL: Analytic queries, window functions, query execution optimization",
                "Linux internals, network performance tuning & distributed systems fundamentals",
                "Data storage formats: Parquet, ORC, Avro, Delta Lake & Apache Iceberg table formats",
                "Object storage architecture (S3, GCS) & blob storage performance tuning",
                "Metadata management, Data Catalogs & Data Lineage concepts",
                "Access control fundamentals: RBAC, ABAC & column/row-level governance",
                "Data quality frameworks: Data contracts, Great Expectations & Soda"
            ],
            "Phase 2: Modern Data Lakehouse & Pipelines": [
                "Data Lakehouse architecture: ACID transactions on object storage (Delta Lake / Iceberg)",
                "Batch processing vs incremental streaming architectures",
                "Building robust ingestion pipelines from heterogeneous sources (APIs, DBs, CDC)",
                "Apache Airflow at enterprise scale: Multi-node clusters, Celery/Kubernetes executors",
                "DAG authoring best practices, dynamic DAG generation & sensor patterns",
                "Idempotency, backfills, failure recovery & automated alerting",
                "Schema evolution handling, backward compatibility & dead letter queues"
            ],
            "Phase 3: Distributed Data Processing & Event Streaming": [
                "Apache Spark internals: Spark core, Catalyst optimizer, Tungsten execution engine",
                "PySpark DataFrames at scale: Broadcast joins, shuffle partitions, skew remediation",
                "Performance optimization: Caching, checkpointing, salting skewed keys",
                "Apache Kafka distributed architecture: Clusters, brokers, partition rebalancing",
                "Kafka event streaming: Exactly-once semantics, consumer lag monitoring",
                "Stream processing with Spark Structured Streaming / Flink basics",
                "Data contracts enforcement between producers and consumers"
            ],
            "Phase 4: Platform Operations, Infrastructure & Governance": [
                "Deploying data infrastructure with Docker & Kubernetes (Spark on K8s)",
                "Infrastructure as Code (Terraform) for provisioning data warehouses and lakehouses",
                "CI/CD automation for data platform code, dbt models & pipeline definitions",
                "Secrets management & secure credential rotation",
                "Observability: Monitoring pipeline health, latency, data freshness & resource utilization",
                "Cloud data platform cost optimization: Compute auto-termination, storage tiering",
                "Governance, audit logging & regulatory compliance (GDPR, SOC2)"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Apache Spark & Catalyst Optimizer, Delta Lake / Apache Iceberg, Apache Kafka, Distributed Systems, Airflow on Kubernetes, Terraform IaC, Data Contracts & Governance.",
            "free_resources": [
                {"title": "Apache Spark Official Architecture Guide", "url": "https://spark.apache.org/docs/latest/"},
                {"title": "Apache Airflow Architecture & Production Guides", "url": "https://airflow.apache.org/docs/"},
                {"title": "Apache Kafka Official Documentation", "url": "https://kafka.apache.org/documentation/"},
                {"title": "Delta Lake Official Documentation", "url": "https://docs.delta.io/latest/index.html"},
                {"title": "Apache Iceberg Table Format Guide", "url": "https://iceberg.apache.org/docs/latest/"}
            ],
            "capstone_project": "Build an Enterprise Scalable Data Lakehouse Platform: Ingestion layer pulls CDC logs to Kafka, Spark Structured Streaming writes into Apache Iceberg tables on S3, Airflow orchestrates daily dimensional dbt transformations, and automated data quality checks enforce data contracts with Slack alerts.",
            "practice_tasks": [
                "Apache Iceberg table create karke time-travel queries aur schema evolution test karo",
                "PySpark me data skewness problem reproduce karke salting technique se fix karo",
                "Kafka producer-consumer setup karke consumer lag monitor karo",
                "Terraform script likho jo data lake object storage buckets aur IAM access policies provision kare"
            ],
            "job_checklist": [
                "Architectural portfolio showing end-to-end distributed data platform on GitHub",
                "Proven experience resolving Spark shuffle spills and data skew bottlenecks",
                "Deep understanding of distributed consensus, table formats (Iceberg/Delta), and Kafka partition topology",
                "Familiarity with data governance, data lineage, and cost optimization"
            ]
        }
    },

    "Software Engineer": {
        "id": "16_software_engineer",
        "icon": "💻",
        "category": "Software Engineering",
        "difficulty": "Beginner to Advanced",
        "duration": "8–14 Months",
        "summary": "Robust, maintainable, scalable aur production-grade software design, development, algorithmic problem solving, automated testing, aur system architecture.",
        "phases": {
            "Phase 1: Programming Foundations & Core Computer Science": [
                "Choose primary language: Python, Java, C++, or TypeScript",
                "Variables, data types, memory model, references vs values",
                "Control structures, loops, recursion & functional programming basics",
                "Data structures: Arrays, linked lists, stacks, queues, hash tables, sets",
                "Object-Oriented Programming (OOP): Encapsulation, inheritance, polymorphism, abstraction",
                "Error handling, exception hierarchies & resource cleanup",
                "Debugging techniques with IDE debuggers, breakpoints & call stack inspection",
                "Git & GitHub: Commits, branches, rebasing, merge conflicts & pull requests"
            ],
            "Phase 2: Data Structures & Algorithms (DSA Mastery)": [
                "Asymptotic analysis: Big-O, Big-Omega, Big-Theta, time & space complexity",
                "Searching algorithms: Linear search, Binary search on arrays & answer spaces",
                "Sorting algorithms: Quicksort, Mergesort, Heapsort, Timsort",
                "Linked Lists: Singly, doubly, circular, fast & slow pointer cycle detection",
                "Stacks & Queues: Monotonic stack, queue using stacks, sliding window maximum",
                "Trees: Binary Trees, Binary Search Trees (BST), traversals (BFS, DFS, Inorder, Preorder, Postorder)",
                "Heaps & Priority Queues: Min-heap, max-heap, Top K elements",
                "Graphs: Adjacency list/matrix, BFS, DFS, Dijkstra shortest path, topological sort",
                "Dynamic Programming: Memoization (top-down), Tabulation (bottom-up), knapsack, LCS"
            ],
            "Phase 3: Software Design, OOP Patterns & Clean Code": [
                "SOLID principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion",
                "Clean Code practices: Descriptive naming, small focused functions, eliminating duplication (DRY)",
                "Creational design patterns: Factory Method, Singleton, Builder",
                "Structural design patterns: Adapter, Decorator, Facade, Composite",
                "Behavioral design patterns: Observer, Strategy, Command, Iterator",
                "Unit testing frameworks (Pytest, JUnit, Jest): Test suites, assertions, test fixtures",
                "Test-Driven Development (TDD) cycle: Red-Green-Refactor",
                "Mocking, stubbing & testing boundary edge cases",
                "Code reviews: Constructive feedback, reviewing for bugs, security & style"
            ],
            "Phase 4: Engineering Practices, Databases & APIs": [
                "HTTP/HTTPS networking basics, client-server models & status codes",
                "RESTful API design: Clean resource endpoints, request validation, pagination",
                "Relational databases (PostgreSQL): Schema design, normalization, joins, indexing",
                "Transactions, ACID properties, isolation levels & database concurrency",
                "Containerization with Docker: Building multi-stage container images",
                "CI/CD pipelines with GitHub Actions: Automated build, test & lint checks",
                "Structured logging, tracing & debugging production issues"
            ],
            "Phase 5: System Design & Scalable Architecture": [
                "System design fundamentals: Functional vs Non-functional requirements",
                "Scalability: Horizontal scaling vs Vertical scaling",
                "Load balancers: Round-robin, least connections, sticky sessions",
                "Caching strategies: In-memory cache (Redis), Cache-Aside, Write-Through, LRU eviction",
                "Database scaling: Read replicas, connection pooling, sharding, partitioning",
                "Asynchronous communication: Message queues (RabbitMQ, Kafka), Pub/Sub, worker tasks",
                "CAP Theorem, Eventual consistency, ACID vs BASE",
                "High availability, fault tolerance, circuit breakers & graceful degradation",
                "Security & Privacy: Authentication, authorization, encryption, rate limiting"
            ]
        },
        "learning_guide": {
            "what_to_learn": "Core DSA (Trees, Graphs, DP), Big-O Analysis, SOLID Principles, Design Patterns, Automated Testing (TDD), PostgreSQL, Docker, System Design (Caching, Queues, Load Balancing).",
            "free_resources": [
                {"title": "NeetCode — Structured DSA & LeetCode Roadmaps", "url": "https://neetcode.io/"},
                {"title": "Refactoring.Guru — Design Patterns & SOLID Principles", "url": "https://refactoring.guru/"},
                {"title": "GitHub Learning Resources Hub", "url": "https://github.com/resources/learn"},
                {"title": "System Design Primer by Donne Martin", "url": "https://github.com/donnemartin/system-design-primer"},
                {"title": "Roadmap.sh Software Design & Architecture", "url": "https://roadmap.sh/software-design-architecture"}
            ],
            "capstone_project": "Build a High-Throughput Asynchronous Task & Job Processing System in Python/TypeScript: REST API accepts computational jobs, pushes to Redis/RabbitMQ queue, worker nodes process in parallel with retry logic, updates PostgreSQL database, covered by 85%+ unit and integration test suite.",
            "practice_tasks": [
                "LeetCode 75 / Blind 75 DSA questions solve karo (Binary Search, Trees, Dynamic Programming)",
                "Strategy pattern aur Factory pattern use karke clean payment processing module design karo",
                "Pytest ya Jest me automated test suite likho with mocks aur parameterized test cases",
                "System design diagram banao for a URL shortener service (TinyURL) handling 100M daily clicks"
            ],
            "job_checklist": [
                "Strong DSA problem-solving track record (150+ medium LeetCode problems)",
                "2 Production-grade software repositories on GitHub with clean commits and unit tests",
                "Mastery of SOLID principles and common software design patterns",
                "Ability to discuss system design trade-offs (Latency vs Throughput, Consistency vs Availability)"
            ]
        }
    },

    "Robotics / Computer Engineer": {
        "id": "17_robotics_computer_engineer",
        "icon": "🤖",
        "category": "Embedded & Hardware",
        "difficulty": "Intermediate to Advanced",
        "duration": "8–14 Months",
        "summary": "Hardware aur low-level software ko combine karke embedded systems, microcontrollers, real-time operating systems (RTOS), aur autonomous robotic systems build karna.",
        "phases": {
            "Phase 1: Computer Hardware & Low-Level Programming (C/C++)": [
                "Digital logic fundamentals: Logic gates, boolean algebra, flip-flops, multiplexers",
                "Computer architecture: CPU registers, ALU, instruction cycle, memory hierarchy, cache",
                "Number systems: Binary, hexadecimal, two's complement, bitwise operators (&, |, ^, ~, <<, >>)",
                "C programming for hardware: Pointers, pointer arithmetic, memory layout (stack, heap, text, bss)",
                "Dynamic memory management: malloc, calloc, free, memory leaks & segmentation faults",
                "Structures, unions, bitfields & hardware register mapping (volatile keyword)",
                "C++ essentials: Classes, constructors/destructors, references, templates, RAII",
                "Basic electronics: Voltage, current, resistance, Ohm's law, capacitors, diodes, transistors",
                "Reading circuit schematics, breadboards, digital multimeters & oscilloscope basics"
            ],
            "Phase 2: Embedded Systems & Microcontrollers": [
                "Microcontroller architecture: Flash, SRAM, EEPROM, clock oscillators, reset circuits",
                "Development boards: ESP32, STM32 (ARM Cortex-M), Arduino, Raspberry Pi Pico",
                "General Purpose Input/Output (GPIO): Digital input, digital output, pull-up/pull-down resistors",
                "Analog-to-Digital Converters (ADC) & Digital-to-Analog Converters (DAC)",
                "Timers, hardware counters & Pulse Width Modulation (PWM) for motor/LED control",
                "Interrupts: Hardware interrupts, Interrupt Service Routines (ISRs), interrupt latency",
                "Communication protocols: UART (serial communication), baud rates, buffers",
                "I2C protocol: Master-slave, addressing, clock stretching, pull-up resistors",
                "SPI protocol: High-speed full-duplex communication (MOSI, MISO, SCK, CS)",
                "Interfacing sensors: Temperature (DHT22), ultrasonic (HC-SR04), IMU (MPU6050 accelerometer/gyro)"
            ],
            "Phase 3: Real-Time Systems & Robotics Fundamentals": [
                "Embedded Linux fundamentals: Cross-compilation, toolchains, device tree, building kernel modules",
                "Real-Time Operating Systems (RTOS): FreeRTOS architecture, tasks, priorities",
                "RTOS synchronization: Semaphores, mutexes, priority inversion, priority inheritance, queues",
                "Actuators & motors: DC motors, H-Bridge drivers (L298N), stepper motors, servo motors",
                "Sensors in robotics: Encoders (odometry), LiDAR scanners, depth cameras",
                "Coordinate frames, transformations, rotation matrices & quaternions",
                "Kinematics: Forward kinematics, inverse kinematics for mobile robots & robotic arms",
                "Feedback control loops: Proportional-Integral-Derivative (PID) controller tuning",
                "Robot simulation: Gazebo simulator, URDF (Unified Robot Description Format)"
            ],
            "Phase 4: Modern Robotics Software (ROS 2)": [
                "ROS 2 (Robot Operating System) architecture: Nodes, topics, publishers, subscribers",
                "ROS 2 Services (request-response) & Actions (long-running goal-oriented tasks)",
                "ROS 2 launch files, parameter management & packaging C++/Python nodes",
                "Sensor data processing: LaserScan, PointCloud2, Odometry, IMU message pipelines",
                "Robot localization: Extended Kalman Filters (EKF), AMCL (Adaptive Monte Carlo Localization)",
                "Simultaneous Localization and Mapping (SLAM): Cartographer, Nav2 SLAM toolbox",
                "Path planning & navigation: Global costmaps, local costmaps, A* algorithm, DWA planner",
                "Computer vision basics for robotics: OpenCV, color filtering, edge detection, object tracking",
                "Testing and validating autonomous robot navigation in simulation and physical hardware"
            ]
        },
        "learning_guide": {
            "what_to_learn": "C/C++ Low-level programming, Bitwise operations, STM32/ESP32 Microcontrollers, FreeRTOS, GPIO/UART/I2C/SPI, Motor Control & PID tuning, ROS 2, Gazebo simulation, SLAM & Nav2.",
            "free_resources": [
                {"title": "ROS 2 Official Documentation & Tutorials", "url": "https://docs.ros.org/"},
                {"title": "Learn C Official Interactive Tutorials", "url": "https://www.learn-c.org/"},
                {"title": "Arduino Official Documentation & Guides", "url": "https://www.arduino.cc/en/Guide"},
                {"title": "FreeRTOS Official Documentation & Architecture", "url": "https://www.freertos.org/"},
                {"title": "Modern Robotics: Mechanics, Planning, and Control (Northwestern Univ)", "url": "https://modernrobotics.northwestern.edu/"}
            ],
            "capstone_project": "Build an Autonomous Mobile Robot Navigation System (Simulated or ESP32/ROS 2): Implements differential drive kinematics, reads LiDAR and IMU data, generates a real-time SLAM occupancy grid map, plans collision-free paths using A*/DWA algorithms, and navigates autonomously to target coordinates with PID motor control.",
            "practice_tasks": [
                "C language me bitwise operations se 8-bit hardware control register manipulate karo",
                "ESP32 par FreeRTOS me 2 concurrent tasks create karo jo queue se sensor data communicate karein",
                "DC motor ke liye PID controller likho jo optical encoder feedback se constant speed maintain kare",
                "ROS 2 C++ node banao jo LiDAR LaserScan topic subscribe karke obstacle alert publish kare"
            ],
            "job_checklist": [
                "GitHub repository with clean C/C++ embedded code, schematics, and ROS 2 packages",
                "Demonstrated mastery of microcontrollers, communication protocols (UART, SPI, I2C), and interrupts",
                "Video demonstration of robot simulation in Gazebo or physical hardware prototype navigating obstacles",
                "Solid understanding of kinematics, PID feedback control, and real-time task scheduling (RTOS)"
            ]
        }
    }
}

# Mapping of track_name -> list of topic strings for backwards compatibility and database queries
BUILTIN_ROADMAPS = {
    track: [topic for phase_topics in catalog_data["phases"].values() for topic in phase_topics]
    for track, catalog_data in ROADMAP_CATALOG.items()
}

# Attach flattened topics list to each ROADMAP_CATALOG item for direct convenience
for track, catalog_data in ROADMAP_CATALOG.items():
    catalog_data["topics"] = BUILTIN_ROADMAPS[track]
