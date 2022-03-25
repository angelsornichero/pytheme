colors ={
  "red": '\033[0;31m',
  "green": '\033[0;32m',
  "yellow": '\033[0;33m',
  "blue":'\033[0;34m',
  "purple":'\033[0;35m',
  "cyan": '\033[0;36m',
}
styles ={
  "bold": '\033[1m',
  "italic": '\033[3m',
  "normal": '\033[0m',
}
def stlprint(
  printed,
  color,
  style,
  
):
  print(styles[style] + colors[color] + printed + styles["normal"])
