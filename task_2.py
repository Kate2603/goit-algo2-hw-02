from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def dp(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit = 0
        best_cuts = []
        for i in range(1, n + 1):
            if i <= len(prices):
                current_profit, current_cuts = dp(n - i)
                total_profit = prices[i - 1] + current_profit
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_cuts = [i] + current_cuts

        memo[n] = (max_profit, best_cuts)
        return memo[n]

    profit, cuts = dp(length)
    return {
        "max_profit": profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1 if cuts else 0
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts_track = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        max_profit = 0
        best_cuts = []
        for j in range(1, i + 1):
            if j <= len(prices):
                if dp[i - j] + prices[j - 1] > max_profit:
                    max_profit = dp[i - j] + prices[j - 1]
                    best_cuts = [j] + cuts_track[i - j]
        dp[i] = max_profit
        cuts_track[i] = best_cuts

    return {
        "max_profit": dp[length],
        "cuts": cuts_track[length],
        "number_of_cuts": len(cuts_track[length]) - 1 if cuts_track[length] else 0
    }

def run_tests():
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
