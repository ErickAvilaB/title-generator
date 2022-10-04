"""" Script to genrate titles """

def main():
  title = "Porcentaje (Programa 10)"

  long = len(title) + 6
  long_row = long - 2
  ascci = 175

  to_print_c = ""
  to_print_n = ""
  spaes = ""

  for i in range(long):
    to_print_c += "%c"
    to_print_n += f", {ascci}"
  
  for i in range(long_row):
    spaes += " "
  
  code = f"""
  printf("{to_print_c}\\n"{to_print_n});
  printf("%c{spaes}%c\\n", {ascci}, {ascci});
  printf("%c  {title}  %c\\n", 175, 175);
  printf("%c{spaes}%c\\n", {ascci}, {ascci});
  printf("{to_print_c}\\n"{to_print_n});
  """

  print(code)

if __name__ == "__main__":
  main()
