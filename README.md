# CustomGPT Template

***Under Development - Most files have not been changed from the parent template.***

This repository provides a foundational template for building large-language model (LLM) applications following the Hexagonal Architecture (also known as Ports and Adapters Architecture) following general guidance in [*Architecture Patterns with Python*](https://learning.oreilly.com/library/view/architecture-patterns-with/9781492052197/) with additions for LLM, data science, machine learning, and natural language process (NLP) workflows. It includes provisions for common components such as web entry points, data storage, and machine learning (ML) models, along with a structured approach to organizing tests, configuration files, and documentation.

## Directory Structure

The directory structure is organized to facilitate a clean separation of concerns, aligning with Hexagonal Architecture principles:

```plaintext
customGPT_template/
│
├── corpora/                # Storage for NLP corpora used in ML or NLP models
│
├── data/                   # Raw and processed datasets for ML and NLP tasks
│   ├── processed/          # Processed datasets ready for analysis or model training
│   ├── raw/                # Unprocessed raw datasets
│   └── README.md           # Documentation for the data directory
│
├── docs/                   # Project documentation, including architecture design
│   ├── design/             # Design documents, diagrams, and architecture notes
│   └── README.md           # Documentation for the docs directory
│
├── notebooks/              # Jupyter notebooks for experimentation and prototyping
│
├── sql/                    # SQL scripts and database migrations
│
├── src/                    # Source code for the application
│   ├── adapters/           # Adapters for interacting with external systems (e.g., databases, APIs)
│   ├── domain/             # Core domain logic and business rules
│   ├── entrypoints/        # Application entry points (e.g., Flask API, CLI, web forms)
│   ├── ml_models/          # Machine learning model implementations and training scripts
│   └── service_layer/      # Application services, orchestrating domain logic and adapters
│   ├── config.py           # Configuration management for the application
│   └── setup.py            # Package configuration for the source code
│
├── tests/                  # Automated tests organized by type
│   ├── e2e/                # End-to-end tests
│   ├── integration/        # Integration tests
│   ├── unit/               # Unit tests
│   ├── conftest.py         # Pytest configuration and fixtures
│   └── pytest.ini          # Pytest configuration file
│
├── web/                    # Web-related assets, if applicable (e.g., static files, templates)
│   └── README.md           # Documentation for the web directory
│
├── .dockerignore           # Files and directories to ignore when building Docker images
├── .gitignore              # Files and directories to ignore in git
├── docker-compose.yml      # Docker Compose configuration for multi-container setups
├── Dockerfile              # Dockerfile for building the application's container
├── mypy.ini                # Configuration for type checking with mypy
├── README.md               # This file
└── requirements.txt        # Python dependencies for the project
```

## How to Use This Template

### 1. **Clone the Repository**

To begin using this template, clone the repository to your local machine:

```bash
git clone https://github.com/ciioprof0/customGPT_template.git
cd customGPT_template
```

### 2. **Install Dependencies**

Make sure you have Python and pip installed. Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

If you plan to use Docker, build the Docker image:

```bash
docker build -t customGPT_template .
```

### 3. **Project Configuration**

Update the `config.py` file in the `src/` directory to suit your project's configuration needs. This file manages settings like database connections, API keys, and environment-specific configurations.

### 4. **Running the Application**

You can run the application using Flask or the entry points defined in the `src/entrypoints/` directory. If using Docker, start the application using Docker Compose:

```bash
docker-compose up
```

### 5. **Running Tests**

The repository is set up with Pytest for testing. To run all tests:

```bash
pytest
```

### 6. **Documentation**

- Design and architecture documentation is located in the `docs/` directory.
- Data handling and processing information can be found in the `data/` directory's README.

### 7. **Developing and Extending**

This template is designed to be extended as per the needs of your specific project. Here are a few common extensions:
- **Adapters**: Add new adapters for different databases, external APIs, or messaging services in the `src/adapters/` directory.
- **ML Models**: Implement machine learning models and related preprocessing scripts in the `src/ml_models/` directory.
- **Entry Points**: Add more entry points (e.g., command-line interfaces or additional web forms) in the `src/entrypoints/` directory.

### 8. **Contributing**

If you wish to contribute to this template, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This `README.md` provides a comprehensive overview of the repository and should serve as a solid starting point for users who wish to leverage this template for their projects.
