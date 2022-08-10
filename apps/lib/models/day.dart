class Day {
  final String posted_by;
  final String todoList;
  final String status;

  Day(
      {this.posted_by = 'Zaineb',
      this.todoList = 'Developing App',
      this.status = 'In-progress'});

  factory Day.fromJson(Map<String, dynamic> json) {
    return Day(
      posted_by: json['posted_by'],
      status: json['status'],
      todoList: json['todoList'],
    );
  }

  Map<String, dynamic> toJson() => {
        'posted_by': posted_by,
        'status': status,
        'todoList': todoList,
      };
}
