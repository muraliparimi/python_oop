


"""
You are given a list of integers and a target integer. Write a Python function that updates the list as follows:
 
Double: For each element in the list that is less than the target integer, replace it with twice its value.

Triple: For each element in the list that is equal to the target integer, replace it with three times its value.

Half: For each element in the list that is greater than the target integer, replace it with half its value (use integer division).
 
 
nums = [5, 10, 15, 20, 25]

target = 15
 
print(update_list(nums, target))

# Output: [10, 20, 45, 10, 12]



You are given a list of dictionaries where each dictionary represents a record of a student’s performance. Each dictionary has the following structure:
{
    "student_id": int,
    "name": str,
    "subject": str,
    "score": int
}

Write a Python function that processes this list and returns a dictionary with the following requirements:
 
Average Scores: For each student, calculate the average score across all subjects.
Highest Score: For each student, find the highest score achieved in any subject.
Lowest Score: For each student, find the lowest score achieved in any subject.
The output should be a dictionary where each key is a student’s student_id, and the value is another dictionary containing the student’s name, average_score, highest_score, and lowest_score.
 
records = [
    {"student_id": 1, "name": "Alice", "subject": "Math", "score": 90},
    {"student_id": 1, "name": "Alice", "subject": "English", "score": 85},
    {"student_id": 1, "name": "Alice", "subject": "Science", "score": 95},
    {"student_id": 2, "name": "Bob", "subject": "Math", "score": 70},
    {"student_id": 2, "name": "Bob", "subject": "English", "score": 75},
    {"student_id": 2, "name": "Bob", "subject": "History", "score": 80},
]
 
print(summarize_student_performance(records))
# Output:
# {
#     1: {
#         "name": "Alice",
#         "average_score": 90.0,
#         "highest_score": 95,
#         "lowest_score": 85
#     },
#     2: {
#         "name": "Bob",
#         "average_score": 75.0,
#         "highest_score": 80,
#         "lowest_score": 70
#     }
# }
# 
# """


def process(nums, target):
    res = []
    for num in nums:
        if num < target:
            res.append(num*2)
        elif num > target:
            res.append(num // 2)
        else:
            res.append(num*3)
    return res

def report_card(records):
    report = {}
    for record in records:
        total = 0
        cnt = 0
        student_id, name, subject, score = record.values()
        if student_id not in report:
            cnt += 1
            report[student_id]  = {"name": name, "highest_score": score, "lowest_score": score, "total": total, "count": cnt }
            print(f"{student_id} is not found and after adding count is {report[student_id]['count']}")
        else:
            print(f"{student_id} is found and its count is {report[student_id]['count']}")
            report[student_id]["highest_score"] = max(report[student_id]["highest_score"], score)
            report[student_id]["lowest_score"] = min(report[student_id]["lowest_score"], score)
            report[student_id]["total"] += score
            report[student_id]["count"] += 1
            print(f"{student_id} is found and and after incereasing count is {report[student_id]['count']}")

    print(report)


    final_report = {}
    for student_id, values in report.items():
        final_report[student_id] = {"name": values["name"], 
                                    "average_score": values["total"]/values["count"], 
                                    "highest_score": values["highest_score"],
                                    "lowest_score": values["lowest_score"]}
    return final_report
        
        
      
if __name__ == '__main__':
    # nums = [5, 10, 15, 20, 25]
    # target = 15
    # res = process(nums, target)
    # print(res)
    records = [{"student_id": 1, "name": "Alice", "subject": "Math", "score": 90},
{"student_id": 1, "name": "Alice", "subject": "English", "score": 85},
{"student_id": 1, "name": "Alice", "subject": "Science", "score": 95},
{"student_id": 2, "name": "Bob", "subject": "Math", "score": 70},
{"student_id": 2, "name": "Bob", "subject": "English", "score": 75},
{"student_id": 2, "name": "Bob", "subject": "History", "score": 80},]
    final_report = report_card(records)
    print(final_report)


"""
table a - 100
table b - 200
A  inner join  B : 100

B left join A : 200

A left join B on a.id = b.id 
where b.id is null  : 0




You are given a table named Sales with the following structure:
 
Sales Table:
 
+--------+-------------+------------+------------+

| SaleID | Salesperson | SaleAmount | SaleDate   |

+--------+-------------+------------+------------+

| 1      | Alice       | 300        | 2024-08-01 |

+--------+-------------+------------+------------+

| 2      | Bob         | 500        | 2024-08-01 |

+--------+-------------+------------+------------+

| 3      | Alice       | 150        | 2024-08-02 |

+--------+-------------+------------+------------+

| 4      | Charlie     | 300        | 2024-08-02 |

+--------+-------------+------------+------------+

| 5      | Bob         | 250        | 2024-08-03 |

+--------+-------------+------------+------------+

| 6      | Alice       | 200        | 2024-08-03 |

+--------+-------------+------------+------------+

| 7      | Charlie     | 200        | 2024-08-03 |

+--------+-------------+------------+------------+

| 8      | Alice       | 400        | 2024-08-04 |

+--------+-------------+------------+------------+

| 9      | Bob         | 100        | 2024-08-04 |

+--------+-------------+------------+------------+

latest_dt as (select salesperson, max(SaleDate)
from sales
group by salesperson)
select * from table a join  latest_dt on a.saless_person = b.sales_person and a.SaleDate = b.SaleDate

-----------------

select *,
dense_rank() over (partition by sales_person order by SaleDate desc) as transaction_rank
from sales




"""

