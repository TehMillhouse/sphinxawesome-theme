---
html_theme:
  description: |
    Learn the different methods to install the Awesome Theme, depending on your use case.
---

(sec:install)=

# Install the theme

```{rst-class} lead
Depending on how you want to use the Awesome Theme,
install it as a Python package or copy it into a local directory.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

(sec:install_python_package)=

## Install the theme as a Python package (recommended)

It's most convenient to install the theme as a Python package.
You can {ref}`customize the theme <sec:customize>` by adding styles or extra templates.

To install the latest **released version** from the Python Package Index
[PyPI](https://pypi.org/project/sphinxawesome-theme/):

```shell-session
pip install sphinxawesome-theme
```

To install the latest **development version** of the theme directly from GitHub:

```shell-session
pip install git+https://github.com/kai687/sphinxawesome-theme.git
```

<!-- vale 18F.UnexpandedAcronyms = NO -->

See the {gh}`CHANGELOG <CHANGELOG.rst>` file for extra features and bugfixes in the
development version that aren't released yet.

<!-- vale 18F.UnexpandedAcronyms = YES -->

## Install the theme as a local package

Installing the theme as a local package can be useful if you want to modify the theme
and test your local modifications. It can also be useful if you want to keep your theme
in a separate directory.

1. {ref}`sec:fork-and-clone`.
1. To install the local version of the theme in your project:

   ```{code-block} shell-session
   ---
   emphasize-text: "/path/to/sphinxawesome_theme"
   ---
   pip install /path/to/sphinxawesome_theme
   ```

   Replace {samp}`{/path/to/sphinxawesome_theme}` with the path to the directory
   containing the `pyproject.toml` file.

(sec:dev-env)=

## Set up a development environment

The project has two different sets of dependencies, for Python and JavaScript. If you
want to write documentation, write tests, or modify the Python extensions,
{ref}`install the Python dependencies <sec:install-python-deps>`.

If you want to modify the Jinja2 templates, the CSS, or the JavaScript files, you also
need to {ref}`install the JavaScript dependencies <sec:install-js-deps>`.

```{note}
It's best to install the JavaScript dependencies, even if you just want to edit the
Jinja2 templates. The theme uses [Tailwind CSS](https://tailwindcss.com) and
[webpack](https://webpack.js.org). If you add new classes from Tailwind, you need to run
webpack to include them in the output CSS.
```

In both cases, create a local copy first.

(sec:fork-and-clone)=

## Create a local copy of the theme

To modify the theme, create a local copy:

1. Optional: [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

   If you don't want to merge your changes with the original repository, you can skip
   this step.

1. Clone the repository:

   - If you forked the repository, enter:

     ```{code-block} shell-session
     ---
     emphasize-text: GITHUB_USERNAME
     ---
     git clone https://github.com/GITHUB_USERNAME/sphinxawesome-theme.git
     ```

     Replace {samp}`{GITHUB_USERNAME}` with your GitHub username.

   - If you didn't fork the repository, clone the original repository:

     ```shell-session
     git clone https://github.com/kai687/sphinxawesome-theme.git
     ```

```{seealso}
[Clone a repository from GitHub](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
```

(sec:install-python-deps)=

## Install Python dependencies

The Awesome Theme uses [Poetry](https://python-poetry.org/) to manage the Python
dependencies and [Nox](https://nox.thea.codes/en/stable/) to test and lint the code.

Follow these steps to install the Python dependencies:

1. Follow the recommended steps for [how to install Poetry](https://python-poetry.org/docs/#installation).

   On macOS and Linux, enter:

   ```shell-session
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
   ```

   On Windows PowerShell:

   ```Powershell
   (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
   ```

1. Install Nox via pip:

   ```shell-session
   pip install --user --upgrade nox
   ```

   If you want to use the same version of Poetry and Nox as the original repository, see
   the versions in the file {gh}`constraints.txt <.github/workflows/constraints.txt>`.

1. Install the Python dependencies:

   ```shell-session
   poetry install
   ```

   Check Poetry's [documentation](https://python-poetry.org/docs/basic-usage/) for more information.

   <!-- vale 18F.Clarity = NO -->

1. Optional: install pre-commit hooks:

   ```shell-session
   poetry run pre-commit install
   ```

   If you don't plan on committing any changes to the forked repository, you can skip
   this step. Check the file {gh}`.pre-commit-config.yaml` to see which pre-commit hooks
   are active.

   To test pre-commit in combination with poetry, run:

   ```shell-session
   poetry run pre-commit run --all
   ```

   <!-- vale 18F.Clarity = YES -->

1. Run a Nox session.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, enter:

   ```shell-session
   nox -ls
   ```

   Enter `nox` without any option to run the default sessions,
   such as building the docs, testing, and linting.

   For example, to build the documentation with Python 3.9, enter:

   ```shell-session
   nox -s docs -p 3.9
   ```

(sec:install-js-deps)=

## Install JavaScript dependencies

Follow these steps to install the JavaScript dependencies:

1. Check, if [Node.js](https://nodejs.org/en/) is installed:

   ```shell-session
   $ node --version
   v14.17.5
   ```

   If the command fails, you may need to install Node.js first,
   or activate it in your current terminal session.
   Have a look at the [Node Version Manager](https://github.com/nvm-sh/nvm)
   project for a way to install and manage multiple versions of Node.js.

1. Optional: install [`yarn`](https://classic.yarnpkg.com/lang/en/):

   ```shell-session
   npm install --global yarn
   ```

   The Awesome Theme uses yarn (classic) and the versions of the npm packages
   are _pinned_ in the `yarn.lock` file.

1. Change the directory to `theme-src/`:

   ```{code-block} shell
   ---
   emphasize-lines: 4
   ---
   ./sphinxawesome-theme/
   ├── src/
   │   ├── sphinxawesome_theme/
   │   └── theme-src/
   ├── docs/
   ├── tests/
   └── ...
   ```

1. Install the JavaScript dependencies:

   ```shell-session
   yarn install
   ```

1. Build the theme:

   ```shell-session
   yarn build
   ```
