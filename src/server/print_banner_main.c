// ==========================================================================
// Print Banner 
// ==========================================================================
// Print a large banner version of a provided input string.
//
// Inf2C-CS Coursework 1. Task B 
// OUTLINE code, to be completed as part of coursework.

// Paul Jackson
//  8 Oct 2013

//---------------------------------------------------------------------------
// C definitions for SPIM system calls
//---------------------------------------------------------------------------
#include <stdio.h>

int read_char() { return getchar(); }
void read_string(char* s, int size) { fgets(s, size, stdin); }

void print_char(int c)     { putchar(c); }   
void print_string(char* s) { printf("%s", s); }

//---------------------------------------------------------------------------
// Global variables
//---------------------------------------------------------------------------

// Size of characters.  
// Use these constants where possible to ease reading and maintaining code

#define NUM_COLS 4
#define NUM_ROWS 5

// Bit-patterns for each character.  
// For simplicity, just have here digits 0-9. 

unsigned int char_pats[] = 
  { 0x69996, // 0
    0x26227, // 1
    0x6924f, // 2
    0xe161e, // 3
    0x26af2, // 4 
    0xf8e1e, // 5
    0x78e96, // 6
    0xf1248, // 7
    0x69696, // 8
    0x6971e  // 9
  };

// Other global variable declarations

// TO BE COMPLETED

//---------------------------------------------------------------------------
// PRINT_BITS
//---------------------------------------------------------------------------
// Print bits n-1 ... 0 of input word w, using a '#' character for each 1 bit,
// and a '.' character for each 0 bit. 

// Assume n > 0

void print_bits(unsigned int w, int n) {
    unsigned int mask = 0x1 << (n - 1);
    while (mask != 0) {
        unsigned int v = w & mask;
        if (v != 0) {
            print_char('#');
        }
        else {
            print_char('.');
        }
        mask = mask >> 1;
    }
    return;
}
//---------------------------------------------------------------------------
// GET_ROW_PATTERN 
//---------------------------------------------------------------------------
// Fetch pattern for row i of ASCII character c

// If c is in the range of the ASCII codes for 0..9, the bit pattern for
// the row is retrieved from the char_pats table.  Otherwise, the function
// always returns 0xf. 

// Rows of a character are numbered from 0, with 0 being the top row.

// TO BE COMPLETED

unsigned int get_row_pattern(char c, int i) {
  return 0xf;
}

//---------------------------------------------------------------------------
// MAIN function
//---------------------------------------------------------------------------
// Prompt for input string up to 12 characters long and generate banner from it. 
//
// If an optional program argument is provided, run a test of the
// get_row_pattern() function instead.
// 
// 
// A remark on handling of command line program arguments in C:
// 
// argc is the number of command line arguments + 1.
// argv is a pointer to an array of strings containing the program name and 
// each of the command line arguments.

// If this program is compiled with 
//   gcc -o banner banner.cc
// Then 
//   ./banner
// gives argc == 1
//   ./banner test
// gives argc == 2.


int main (int argc, char** argv) {

    unsigned int pat;
	int optional = 0;

    if (argc > 1) {
	int i;
	for (i = 1; i < argc; i++) { //skip argv[0] program name
		if (strcmp(argv[i], "-o") == 0) { //optional argument -o

		// Test code for get_row_pattern().
		// Assumes print_bits() is functioning properly.

		// If all is good, this outputs the top 2 rows for character '4': 
		// ....#.
		// ...##.

		// As '4' is not symmetric across horizontal or vertical axis, these
		// tests should catch errors where horizontal or vertical indexing is
		// reversed.

			unsigned int pat;
			pat = get_row_pattern('4', 0);
        		print_bits(pat, NUM_COLS+2);
        		print_char('\n');
        		pat = get_row_pattern('4', 1);
			print_bits(pat, NUM_COLS+2);
			print_char('\n');
			print_char('\n');
			return 0;
		}
	}	
		// Main code
    		// TO BE COMPLETED
		
		/* first iterating through the rows so first I print the whole first line of
		*/
	int j;
	for (j = 0; j < NUM_ROWS-1; j++) {
		
			int k;
			for (k = 0; k < strlen(argv[1]); k++) {
				/* 	C code of the implementation of string lengths 
					could come handy for MIPS

				size_t strlen (char *str) {
				size_t len = 0; 
				while (*str != '\0') {
					str++;
					len++;
				}
				return len;
				}*/
					
				int pati;
				pati = get_row_pattern(argv[1][k], j); /* bit pattern of the jth row of the kth char */
				print_bits(pati, NUM_COLS+2); //printing bit pattern and an extra 2 dots
				print_char('\n'); //after printing everything in a row finally a new line
			}
	} 
		  

    

    return 0;
}


//---------------------------------------------------------------------------
// End of file
//---------------------------------------------------------------------------

