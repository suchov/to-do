import zipfile


def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/home/artem/projects/python/apps/to-do/compressed.zip",
                    "/home/artem/projects/python/apps/to-do/")
