def repiece(squashed: list[str], width:int, height:int, file_name: str) -> None:
    with open(file_name, "w") as f:
        for x in range(0, height):
            f.write("".join(squashed[x*width:(x+1)*width]) + '\n') 