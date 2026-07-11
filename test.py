from checkers import run_all_checks
from scorer import calculate_score

url = input("Enter URL: ")

results = run_all_checks(url)

final_result = calculate_score(results)

print("\n============================")
print("PHISHGUARD REPORT")
print("============================")

print(f"\nRisk Score : {final_result['score']}/100")
print(f"Verdict    : {final_result['verdict']}")

print("\nReasons:")

if final_result["reasons"]:
    for reason in final_result["reasons"]:
        print("-", reason)
else:
    print("No suspicious indicators found.")