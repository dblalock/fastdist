//
//  Dist.h
//  Dig
//
//  Created by DB on 10/2/14.
//  Copyright (c) 2014 DB. All rights reserved.
//

#ifndef Dig_Dist_h
#define Dig_Dist_h

//==================================================
// Constants
//==================================================

typedef enum DistanceMeasure {
	EUCLIDEAN = 0,
	ED = EUCLIDEAN,
	DYNAMIC_TIME_WARPING = 1,
	DTW = DYNAMIC_TIME_WARPING,
} DistanceMeasure;


class DTWFixedLenIndex {
private:
	class impl;
	std::unique_ptr<impl> _pimpl;
public:
	DTWFixedLenIndex(size_t nsamples, size_t ndims, bool tie_dims=true);
	~DTWFixedLenIndex();

	void set_tie_dims(bool tie_dims);
	void addExample(const float* X, int m, int n, int label);
	// void addExamples(const float* x, int m, int n, int label);
	int knn(const float* q, int m, int n);
};

//==================================================
// Distance Measures
//==================================================

// ------------------------------- L1 distance

int dist_L1(const int* v1, const int* v2, int n);
int dist_L1(const int* v1, int m, const int* v2, int n);
double dist_L1(const double* v1, const double* v2, int n);
double dist_L1(const double* v1, int m, const double* v2, int n);

// ------------------------------- L2 distance

int dist_L2(const int* v1, const int* v2, int n);
int dist_L2(const int* v1, int m, const int* v2, int n);
double dist_L2(const double* v1, const double* v2, int n);
double dist_L2(const double* v1, int m, const double* v2, int n);

// ------------------------------- DTW distance

int dist_dtw(const int* v1, const int* v2, int n, int r);
int dist_dtw(const int* v1, int m, const int* v2, int n, int r);
double dist_dtw(const double* v1, const double* v2, int n, int r);
double dist_dtw(const double* v1, int m, const double* v2, int n, int r);

#endif // Dig_Dist_h
