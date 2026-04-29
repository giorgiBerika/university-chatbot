from pathlib import Path 

def load_data( path ) -> list:
    try:
        folder_path = Path( path )
        result = []
        for file in folder_path.glob("*.txt"):
            with open( file, "r", encoding="utf-8" ) as f:
                content = f.read()
                result.append( {"text": content, 
                                "source": file.name } )

        return result
    except FileNotFoundError:
        return []
    