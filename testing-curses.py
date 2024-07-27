import curses

def display_menu(stdscr, options, question):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    selected_indices = set()
    current_index = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(1, width // 2 - len(question) // 2, question)

        for idx, option in enumerate(options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(options) // 2 + idx + 2
            if idx == current_index:
                stdscr.attron(curses.color_pair(1))
            if idx in selected_indices:
                stdscr.addstr(y, x - 4, "[x] ")
            else:
                stdscr.addstr(y, x - 4, "[ ] ")
            stdscr.addstr(y, x, option)
            if idx == current_index:
                stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_DOWN and current_index < len(options) - 1:
            current_index += 1
        elif key == ord(' '):
            if current_index in selected_indices:
                selected_indices.remove(current_index)
            else:
                selected_indices.add(current_index)
        elif key == ord('\n'):
            break

    return [options[i] for i in selected_indices]

def main(stdscr):
    options = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    question = "Choose from the following options:"

    selected_items_1 = display_menu(stdscr, options, question)
    selected_items_2 = display_menu(stdscr, options, question)

    curses.endwin()  # Restore terminal to original state

    print("You selected for the first question:")
    for item in selected_items_1:
        print(f"- {item}")

    print("\nYou selected for the second question:")
    for item in selected_items_2:
        print(f"- {item}")

    name = input("\nEnter your name: ")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    curses.wrapper(main)
