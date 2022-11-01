
def main():
    createMap()
    generateLevel()
    createPlayer()
    while (True):
        getInput()
        movePlayer()
        displayMap()

if __name__ == '__main__':
    main()