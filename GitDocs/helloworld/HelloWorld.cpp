//input and output functions are included in iostream file,
//which define 4 IO objects: cout, cin, cerr, clog
#include <iostream>

//namespace is used to prevent the interruption among the global names,
//building walls between every program library.
//It could distinguish the difference between two var or fun in different place which have a //same name.
using namespace std;

//the first namespace, same function func()
namespace first_space{
	void func(){
		cout << "Helloworld 1" << endl;
	}
}

//the second namespace, same function func()
namespace second_space{
	void func(){
		//output "HelloWorld 2xixixi"
		cout << "HelloWorld 2" << "xixxixi" << endl;
	}
}

int main()
{
	//call func() in the first namespace
	first_space::func();

	//call func() in the second namespace
	second_space::func();
	
	return 0;
}

//endl: a functional template, inserting newline and flushing output stream
//TO UNDERSTANDING
//just edit it!
//edit again!
//<< : a shift operator, but here it's a reloaded operator function. 

