# How to create a script that accept an argument

## Script 

```
def open_document(file_name):
    document = os.path.normpath(os.path.join(DOCUMENT_DIR, file_name))
    with open(document) as fp:
        return json.load(fp, object_pairs_hook=OrderedDict)

def process(file_name):
    document = open_document(document_name)
    print(json.dumps(document, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--document_name", help = "Automation Document Name", nargs="*",
                        default = None)
    args = parser.parse_args()
    process(args.document_name[0])
```

## Command 
```
script.py --file $(FILE_NAME) > ./Output/$(FILE_NAME)
```

