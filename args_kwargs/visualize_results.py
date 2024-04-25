import matplotlib.pyplot as plt

def visualize_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # 可视化结果的代码
        plt.plot(result)
        plt.show()
        return result
    return wrapper

@visualize_results
def calculate_values():
    # 计算数值的代码
    values = [1, 2, 3, 4, 5]
    return values

calculate_values()
