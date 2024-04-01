import argparse
import hashlib


def generate_hash(algorithm, data):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(data.encode())
    return hash_obj.hexdigest()

def generate_file_hash(algorithm, file_path):
    hash_obj = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def compare_hashes(expected_hash, actual_hash):
    return expected_hash == actual_hash

def main():
    parser = argparse.ArgumentParser(description="python hash tool")
    
    parser.add_argument('option', choices=['sthash', 'filehash', 'comp'], help='使用するオプション')
    parser.add_argument('--algorithm', choices=['md5', 'sha1', 'sha256', 'sha384', 'sha512'], help='ハッシュアルゴリズム')
    parser.add_argument('--string', help='ハッシュする文字列')
    parser.add_argument('--file', help='ファイルパス')
    parser.add_argument('--hash', help='期待されるハッシュ値')

    args = parser.parse_args()

    if args.option == 'sthash':
        if not (args.algorithm and args.string):
            parser.error('--algorithmと--stringは必須です')
        hash_value = generate_hash(args.algorithm, args.string)
        print(f'ハッシュ値: {hash_value}')

    elif args.option == 'filehash':
        if not (args.algorithm and args.file):
            parser.error('--algorithmと--fileは必須です')
        hash_value = generate_file_hash(args.algorithm, args.file)
        print(f'ファイルのハッシュ値: {hash_value}')

    elif args.option == 'comp':
        if not (args.hash and (args.string or args.file)):
            parser.error('--hashと--stringまたは--fileは必須です')
        if args.string:
            actual_hash = generate_hash(args.algorithm, args.string)
        elif args.file:
            actual_hash = generate_file_hash(args.algorithm, args.file)
        if compare_hashes(args.hash, actual_hash):
            print('ハッシュ値は一致しています')
        else:
            print('ハッシュ値が一致しません')

if __name__ == '__main__':
    main()