def count_by_extension(paths):

    extensions = {}

    for path in paths:
        if '.' in path:
            extension = path.split('.')[-1].lower()
        else:
            extension = ""
        extensions[extension] = extensions.get(extension, 0) + 1

    return extensions


def deepest_path(paths):

    if len(paths) == 0:
        return ""
    
    deepest = paths[0]
    max_depth = deepest.count('/')

    for path in paths:
        depth = path.count('/')
        if depth > max_depth:
            deepest = path
            max_depth = depth

        if depth == max_depth and path < deepest:
            deepest = path

    return deepest

def human_size(n_bytes):

    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    size = n_bytes
    i = 0

    while size >= 1024 and i < 4:
        size = size / 1024
        i = i + 1
    if i == 0:
        return str(size) + ' ' + units[i]
    else:
        return str(round(size, 1)) + ' ' + units[i]
    


paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

print(count_by_extension(paths))   # {"pdf": 1, "txt": 1, "png": 1, "": 1}

print(deepest_path(paths))         # "docs/img/logo.png"

print(human_size(900))             # "900 Б"
print(human_size(1536))            # "1.5 КБ"
print(human_size(5 * 1024 * 1024)) # "5.0 МБ"