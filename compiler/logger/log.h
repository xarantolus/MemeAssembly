#ifndef LOG_H
#define LOG_H

#include <stdio.h>  //Printf() function
#include <stdlib.h> //Exit() function

void setLogLevel(int newLogLevel);

void printInformationHeader();

void printErrorASCII();

void printThanosASCII(int deletedLines);

void printSuccessMessage(char message[]);
void printStatusMessage(char message[]);
void printInfoMessage(char message[]);
void printDebugMessage(char message[], char *variable);
void printDebugMessageWithNumber(char message[], int variable);

void printSemanticError(char message[], int lineNum);
void printSemanticErrorWithExtraLineNumber(char message[], int lineNum, int originalDefinition);

void printUnexpectedCharacterError(char expected[], char got[], int lineNum);
void printSyntaxError(char message[], char got[], int lineNum);
void printSyntaxErrorWithoutString(char message[], int lineNum);

#endif