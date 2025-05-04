from utils import parse_figure

def find_max_figure(file_path):
    max_value = -1
    max_figure = None

    with open(file_path) as f:
        for line in f:
            fig = parse_figure(line)
            value = fig.volume()
            if value and value > max_value:
                max_value = value
                max_figure = fig

    return max_figure, max_value


if __name__ == "__main__":
    file = "input01.txt"  # or input02.txt / input03.txt
    fig, value = find_max_figure(file)
    print(f"Figure with max measure is: {fig.__class__.__name__}, measure = {value:.2f}")

