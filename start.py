#start02
from PIL import Image

# Percorso dell'immagine
input_path = "root/supporto/image0.png"  # Percorso corretto al file
output_path = "root/supporto/image0_with_white_background.png"  # Percorso per salvare l'immagine risultante

# Carica l'immagine
img = Image.open(input_path).convert("RGBA")

# Crea un'immagine bianca con le stesse dimensioni
white_background = Image.new("RGBA", img.size, "WHITE")

# Sovrapponi l'immagine originale sopra lo sfondo bianco
composite = Image.alpha_composite(white_background, img)

# Converti in RGB per rimuovere il canale alpha
composite = composite.convert("RGB")

# Salva l'immagine risultante
composite.save(output_path)

print(f"Immagine con sfondo bianco salvata in: {output_path}")
