class FileSystem:
    
    def __init__(self):
        self.fs = {}
    
    def add_directory(self, path: str) -> bool:
        fs_parts = path.strip("/").split("/")
        current_dir = self.fs
        
        for part in fs_parts:
            if part not in current_dir:
                current_dir[part] = {}
            current_dir = current_dir[part]
        self.fs = current_dir

    def add_file(self, path: str, content: str) -> bool:
        fs_parts = path.strip("/").split("/")
        current_dir = initial_dir = self.fs
        for part in fs_parts[:len(fs_parts) - 1]:
            current_dir = current_dir[part]
        if fs_parts[-1] not in current_dir:
            current_dir[fs_parts[-1]] = content
            self.fs = 
            return True
        else:
            return False
    
    def get_content(self, path: str) -> str | None:
        fs_parts = path.strip("/").split("/")
        current_dir = self.fs
        for part in fs_parts[:len(fs_parts) - 1]:
            current_dir = current_dir[part]
        try:
            return current_dir[fs_parts[-1]]
        except KeyError:
            return None
        
    def delete(self, path: str) -> bool:
        fs_parts = path.strip("/").split("/")
        current_dir = self.fs
        for part in fs_parts[:len(fs_parts) - 1]:
            current_dir = current_dir[part]
        try:
            del current_dir[fs_part[-1]]
            self.fs = current_dir
            