"""
The script clones git remote repo to the local path.

Example of the usage:
python clone_git_repo.py --git-url https://github.com/denissmi/clone_git_repo --branch master
--local_path C:\clone_git_repo
"""
import argparse
import git
import pathlib


def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--git-url', dest='git_url', required=True, help='Gir repo URL address')
    parser.add_argument('--branch', dest='branch', default='master', help='Repo branch')
    parser.add_argument('--local-path', dest='local_path', type=pathlib.Path, default=pathlib.Path(),
                        help='Path to local repo')

    return parser.parse_args()


def main():
    """The mian function."""
    args = parse_arguments()
    if args.local_path.exists():
        repo = git.Repo(args.local_path)
    else:
        repo = git.Repo.clone_from(args.git_url, args.local_path, branch=args.branch)


if __name__ == '__main__':
    main()
