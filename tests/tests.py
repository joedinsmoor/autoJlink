import os
import tempfile
import pytest

def copy_file(src_path, dest_path):
    with open(src_path, 'rb') as src_file:
        with open(dest_path, 'wb') as dest_file:
            dest_file.write(src_file.read())

def compare_files(file1, file2):
    with open(file1, 'rb') as f1:
        with open(file2, 'rb') as f2:
            return f1.read() == f2.read()

@pytest.fixture
def temp_files(request):
    src_content = b'This is the source file content.'
    src_file = tempfile.NamedTemporaryFile(delete=False)
    src_file.write(src_content)
    src_file.close()

    dest_file = tempfile.NamedTemporaryFile(delete=False)
    dest_file.close()

    def cleanup():
        os.unlink(src_file.name)
        os.unlink(dest_file.name)

    request.addfinalizer(cleanup)

    return src_file.name, dest_file.name

def test_copy_and_compare(temp_files):
    src_file, dest_file = temp_files

    copy_file(src_file, dest_file)

    assert compare_files(src_file, dest_file), "Copied contents are not the same."
