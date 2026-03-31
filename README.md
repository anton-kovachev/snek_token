# 🐍 Snek Token

A modern ERC20 token implementation built with Vyper, showcasing secure smart contract development practices and comprehensive testing strategies.

## 📋 Overview

Snek Token is an ERC20-compliant token contract that demonstrates professional smart contract development using the Vyper language. The project leverages the [snekmate](https://github.com/pcaversaccio/snekmate) library for battle-tested, audited contract modules and includes extensive testing with both unit and property-based fuzzing tests.

### Key Features

- ✅ **ERC20 Standard Compliance** - Full implementation of the ERC20 token standard
- 🔒 **Ownable Pattern** - Built-in access control using snekmate's ownable module
- 🧪 **Comprehensive Testing** - Unit tests, stateful fuzzing, and invariant tests
- 🐍 **Vyper Smart Contracts** - Written in Vyper 0.4.3 for enhanced security
- 🛠️ **Modern Tooling** - Built with Moccasin framework and titanoboa

## 🏗️ Business Case

This project serves as a reference implementation for:
- **Token Launches** - Demonstration of secure token deployment practices
- **Educational Purposes** - Learning Vyper and smart contract security
- **Testing Strategies** - Showcase of property-based testing for smart contracts
- **Code Quality** - Example of maintainable and auditable smart contract code

## 🔧 Technologies Used

- **[Vyper](https://docs.vyperlang.org/)** (v0.4.3) - Smart contract programming language
- **[Moccasin](https://cyfrin.github.io/moccasin)** - Python-based smart contract development framework
- **[snekmate](https://github.com/pcaversaccio/snekmate)** - Vyper contract library with audited implementations
- **[titanoboa](https://github.com/vyperlang/titanoboa)** - Vyper interpreter and testing framework
- **[Hypothesis](https://hypothesis.readthedocs.io/)** - Property-based testing library
- **Python** (≥3.11) - Development environment
- **[just](https://github.com/casey/just)** - Command runner for project tasks

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/anton-kovachev/snek_token.git
   cd snek_token
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```
   
   Or with uv:
   ```bash
   uv pip install -e .
   ```

4. **Verify installation**
   ```bash
   mox --version
   ```

## 🚀 Usage

### Deploy Contract

Deploy to a local test network (titanoboa automatically spins up a test environment):

```bash
mox run deploy
```

### Run Tests

Execute all tests:
```bash
mox test
```

Run specific test categories:
```bash
# Unit tests only
mox test tests/test_token.py

# Stateful fuzzing tests
mox test tests/invariant/test_stateful.py

# Stateless fuzzing tests
mox test tests/invariant/test_stateless.py
```

### Format Code

Format Vyper contracts:
```bash
just format
```

## 📁 Project Structure

```
mox-erc20-cu/
├── contracts/
│   ├── snek_token.vy           # Main ERC20 token contract
│   └── invariant/              # Contracts for invariant testing
├── tests/
│   ├── test_token.py           # Unit tests
│   ├── conftest.py             # Test fixtures
│   └── invariant/              # Property-based fuzz tests
├── script/
│   └── deploy.py               # Deployment script
├── lib/                        # Dependencies (snekmate)
├── pyproject.toml              # Project configuration
├── justfile                    # Task runner commands
└── README.md
```

## 🧪 Testing Strategy

This project implements a comprehensive testing approach:

1. **Unit Tests** - Verify individual function behavior and expected outcomes
2. **Stateful Fuzzing** - Use Hypothesis to test state transitions and invariants
3. **Stateless Fuzzing** - Property-based testing for pure functions

The tests are designed to catch common vulnerabilities and ensure contract invariants hold under all conditions.

## 🔐 Security Considerations

⚠️ **Note**: This contract includes a deliberate bug in the `super_mint()` function for educational purposes. The function mints tokens without updating the total supply - this is intentionally vulnerable to demonstrate the importance of proper testing and invariant checks.

**Do not use this contract in production without removing the vulnerable `super_mint()` function.**

## 📚 Contract Details

- **Token Name**: snek_token
- **Symbol**: SNEK
- **Decimals**: 18
- **Initial Supply**: 1,000 SNEK (configurable in deployment script)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the contract header for details.

## 🙏 Acknowledgments

- [snekmate](https://github.com/pcaversaccio/snekmate) - For providing audited Vyper contract modules
- [Moccasin](https://cyfrin.github.io/moccasin) - For the excellent Python-based development framework
- [Cyfrin](https://www.cyfrin.io/) - For educational resources and tooling

## 📞 Contact

Anton Kovachev - [@anton-kovachev](https://github.com/anton-kovachev)

Project Link: [https://github.com/anton-kovachev/snek_token](https://github.com/anton-kovachev/snek_token)

---

_For more detailed Moccasin documentation, run `mox --help` or visit [the Moccasin documentation](https://cyfrin.github.io/moccasin)_
