import argparse
import json
import converter

def main():
    convert = get_args()

    print(convert.convert())


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', type=str, help='File to convert')
    parser.add_argument('-n', '--new_format', type=str, help='New format')
    parser.add_argument('-c', '--config_file', type=str, help='Config file')

    args = parser.parse_args()
    parsing_with_config_file(args)

    input_file = getattr(args, 'input_file')
    new_format = getattr(args, 'new_format')

    convert = converter.Converter(input_file, new_format)

    return convert


def parsing_with_config_file(args):
    if not args.config_file:
        return
    try:
        with open(args.config_file, 'r') as rf:
            config = json.load(rf)
            args.input_file = config['file_to_convert']
            args.new_format = config['new_file_format']
    except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
        raise("Invalid config file")


if __name__ == "__main__":
    main()