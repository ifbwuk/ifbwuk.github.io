import curses

def main(stdscr):
    # Initialize the window and make the cursor visible
    curses.curs_set(1)
    stdscr.clear()
    
    # Display some text to interact with
    text = "Hello, this is a test. Move the cursor around!"
    stdscr.addstr(0, 0, text)
    stdscr.refresh()
    
    # Wait for user input
    stdscr.addstr(2, 0, "Move the cursor over the text and press any key to see the letter under the cursor.")
    stdscr.refresh()

    # Wait for the user to press a key
    stdscr.getch()

    # Get the current cursor position
    y, x = curses.getsyx()

    # Read the character at the cursor's position
    char_under_cursor = stdscr.instr(y, x, 1).decode('utf-8')

    # Show the character under the cursor
    stdscr.addstr(3, 0, f"The character under the cursor is: '{char_under_cursor}'")
    stdscr.refresh()

    # Wait for the user to exit
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
