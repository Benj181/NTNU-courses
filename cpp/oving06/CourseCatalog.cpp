#include "CourseCatalog.h"

// BEGIN: 3a
void CourseCatalog::addCourse(const string& key, const string& value){
    courses.insert({key, value});
}
// END: 3a

// BEGIN: 3b
void CourseCatalog::removeCourse(const string& key){
    courses.erase(key);
}
// END: 3b

// BEGIN: 3c
string CourseCatalog::getCourse(const string& key) const{
    return courses.at(key);
}
// END: 3c

// BEGIN: 3d
ostream& operator<<(ostream& os, const CourseCatalog& cc){
    for (const auto& course : cc.courses) {
        os << course.first << " " << course.second << "\n";
    }
    return os;
    
}
// END: 3d

// BEGIN: 3e
void testCourseCatalog(){
    CourseCatalog cc;
    cc.addCourse("TDT4110", "Informasjonsteknologi grunnkurs");
    cc.addCourse("TDT4102", "Prosedyre- og objektorientert programmering");
    cc.addCourse("TMA4100", "Matematikk 1");
    cout << cc << endl;
    cc.addCourse("TDT4102", "cpp");
    cout << cc << endl;
}
// END: 3e

// BEGIN: 3g
void CourseCatalog::saveToFile(const std::string& filename) const{
    std::ofstream os{filename};
    for (const auto& course : courses){
        os << course.first << ":" << course.second << "\n";
    }
}
// END: 3g

// BEGIN: 3h
void CourseCatalog::loadFromFile(const std::string& filename){
    std::ifstream is{filename};
	
    if (!is){
		std::cout << "File does'nt exist" << std::endl;
		exit(0);
	}

    std::string line;
    while(std::getline(is, line)){
        auto delimiterPos = line.find(":");
        auto key = line.substr(0, delimiterPos);
        auto value = line.substr(delimiterPos + 1);
        courses.insert({key, value});
    }
}
// END: 3h


void testReadAndWrite(){
    CourseCatalog cc;
    cc.addCourse("TDT4110", "Informasjonsteknologi grunnkurs");
    cc.addCourse("TDT4102", "Prosedyre- og objektorientert programmering");
    cc.addCourse("TMA4100", "Matematikk 1");

    cout << cc << endl;

    cc.saveToFile("test.txt");

    cc.removeCourse("TDT4110");
    cc.removeCourse("TDT4102");
    cc.removeCourse("TMA4100");

    cout << "Test" << endl;
    cout << cc << endl;

    cc.loadFromFile("test.txt");

    cout << cc << endl;
}