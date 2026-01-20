import pandas as pd

# rutas
INPUT_PATH = "data/raw.csv"
OUTPUT_PATH = "data/clean.csv"

def main():
    # leer datos
    df = pd.read_csv(INPUT_PATH)

    print("Filas originales:", len(df))

    # eliminar filas completamente vacías
    df = df.dropna(how="all")

    # eliminar duplicados
    df = df.drop_duplicates()

    # limpiar texto (si existe la columna titulo)
    if "titulo" in df.columns:
        df["titulo"] = df["titulo"].str.strip()

    print("Filas limpias:", len(df))

    # guardar archivo limpio
    df.to_csv(OUTPUT_PATH, index=False)
    print("Archivo clean.csv creado")

if __name__ == "__main__":
    main()
