#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fs
Version  : 1.2.6
Release  : 2
URL      : https://cran.r-project.org/src/contrib/fs_1.2.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fs_1.2.6.tar.gz
Summary  : Cross-Platform File System Operations Based on 'libuv'
Group    : Development/Tools
License  : CC-BY-4.0 GPL-3.0 MIT
Requires: R-fs-lib = %{version}-%{release}
BuildRequires : R-Rcpp
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
top of the 'libuv' C library.

%package lib
Summary: lib components for the R-fs package.
Group: Libraries

%description lib
lib components for the R-fs package.


%prep
%setup -q -c -n fs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540748727

%install
export SOURCE_DATE_EPOCH=1540748727
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fs|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fs/COPYRIGHTS
/usr/lib64/R/library/fs/DESCRIPTION
/usr/lib64/R/library/fs/INDEX
/usr/lib64/R/library/fs/Meta/Rd.rds
/usr/lib64/R/library/fs/Meta/features.rds
/usr/lib64/R/library/fs/Meta/hsearch.rds
/usr/lib64/R/library/fs/Meta/links.rds
/usr/lib64/R/library/fs/Meta/nsInfo.rds
/usr/lib64/R/library/fs/Meta/package.rds
/usr/lib64/R/library/fs/NAMESPACE
/usr/lib64/R/library/fs/NEWS.md
/usr/lib64/R/library/fs/R/fs
/usr/lib64/R/library/fs/R/fs.rdb
/usr/lib64/R/library/fs/R/fs.rdx
/usr/lib64/R/library/fs/WORDLIST
/usr/lib64/R/library/fs/help/AnIndex
/usr/lib64/R/library/fs/help/aliases.rds
/usr/lib64/R/library/fs/help/fs.rdb
/usr/lib64/R/library/fs/help/fs.rdx
/usr/lib64/R/library/fs/help/paths.rds
/usr/lib64/R/library/fs/html/00Index.html
/usr/lib64/R/library/fs/html/R.css
/usr/lib64/R/library/fs/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fs/libs/fs.so
/usr/lib64/R/library/fs/libs/fs.so.avx2
/usr/lib64/R/library/fs/libs/fs.so.avx512