Create a virtual environment
```bash
python -m venv ./venv
```
activate env
```bash
source venv/Scripts/activate
```

create requirements file

install requirements
```bash
pip install -r requirements.txt
```

download the data from

https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/winequality.csv
```

```bash
dvc init
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

onliner update for README
```bash
git add. && git commit -m "README file changed"
```

```bash
git remote add origin https://github.com/SubhamZap/Wine-Quality.git
git branch -M main
git push origin main
```