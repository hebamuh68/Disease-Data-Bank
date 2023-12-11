def handle_uploaded_file(f):
    file_path = 'PDB/static/upload/' + f.name
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path
