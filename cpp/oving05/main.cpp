#include "std_lib_facilities.h"
#include "Card.h"
#include "CardDeck.h"

int main(){
	CardDeck cd{};
	cd.shuffle();
	cd.print();
	cout << "----------------------" << endl;
	cout << cd.drawCard().toString() << endl;
	cout << "----------------------" << endl;
	cd.print();
	return 0;
}