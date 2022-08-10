import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_calendar/calendar.dart';

class CalendarPage extends StatelessWidget {
  const CalendarPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
      child: SfCalendar(
        view: CalendarView.month,
      ),
    ));
  }

  // @override
  // Widget build(BuildContext context) {
  //   return Container(
  //     child: const Text("HELLOOO"),
  //   );
  // }
}
