#pragma once
#include "std_lib_facilities.h"

class CourseCatalog
{
public:
	void addCourse(const string& key, const string& value);
	void removeCourse(const string& key);
	string getCourse(const string& key) const;

	friend ostream& operator<<(ostream& os, const CourseCatalog& cc);
	
	void saveToFile(const std::string& filename) const;
	void loadFromFile(const std::string& filename);

private:
	map<string, string> courses;
};

void testCourseCatalog();