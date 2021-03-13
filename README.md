# Bitwarden Scripts
Scripts to manage Bitwarden passwords

## Usage

### Installation
`brew install bitwarden-cli`

### Get Full Password Output
`bw export --output ./bw.json --format json`
(this will ask for your master password)

### Script Usage
with a bw.json file in the path, run one of the scripts:
`python3 essential_csv.py`
