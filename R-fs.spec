#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fs
Version  : 1.3.1
Release  : 14
URL      : https://cran.r-project.org/src/contrib/fs_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fs_1.3.1.tar.gz
Summary  : Cross-Platform File System Operations Based on 'libuv'
Group    : Development/Tools
License  : CC-BY-4.0 GPL-3.0 MIT
Requires: R-fs-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-purrr
BuildRequires : R-Rcpp
BuildRequires : R-purrr
BuildRequires : buildreq-R

%description
## Overview
libuv is a multi-platform support library with a focus on asynchronous I/O. It
was primarily developed for use by [Node.js][], but it's also
used by [Luvit](http://luvit.io/), [Julia](http://julialang.org/),
[pyuv](https://github.com/saghul/pyuv), and [others](https://github.com/libuv/libuv/wiki/Projects-that-use-libuv).

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
export SOURCE_DATE_EPOCH=1557193984

%install
export SOURCE_DATE_EPOCH=1557193984
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
R CMD check --no-manual --no-examples --no-codoc fs || :


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
/usr/lib64/R/library/fs/Meta/vignette.rds
/usr/lib64/R/library/fs/NAMESPACE
/usr/lib64/R/library/fs/NEWS.md
/usr/lib64/R/library/fs/R/fs
/usr/lib64/R/library/fs/R/fs.rdb
/usr/lib64/R/library/fs/R/fs.rdx
/usr/lib64/R/library/fs/WORDLIST
/usr/lib64/R/library/fs/doc/function-comparisons.R
/usr/lib64/R/library/fs/doc/function-comparisons.Rmd
/usr/lib64/R/library/fs/doc/function-comparisons.html
/usr/lib64/R/library/fs/doc/index.html
/usr/lib64/R/library/fs/help/AnIndex
/usr/lib64/R/library/fs/help/aliases.rds
/usr/lib64/R/library/fs/help/fs.rdb
/usr/lib64/R/library/fs/help/fs.rdx
/usr/lib64/R/library/fs/help/paths.rds
/usr/lib64/R/library/fs/html/00Index.html
/usr/lib64/R/library/fs/html/R.css
/usr/lib64/R/library/fs/tests/spelling.R
/usr/lib64/R/library/fs/tests/testthat.R
/usr/lib64/R/library/fs/tests/testthat/blns.txt.xz
/usr/lib64/R/library/fs/tests/testthat/helper.R
/usr/lib64/R/library/fs/tests/testthat/ref-tree-1
/usr/lib64/R/library/fs/tests/testthat/ref-tree-2
/usr/lib64/R/library/fs/tests/testthat/ref-tree-3
/usr/lib64/R/library/fs/tests/testthat/test-access.R
/usr/lib64/R/library/fs/tests/testthat/test-copy.R
/usr/lib64/R/library/fs/tests/testthat/test-create.R
/usr/lib64/R/library/fs/tests/testthat/test-delete.R
/usr/lib64/R/library/fs/tests/testthat/test-file.R
/usr/lib64/R/library/fs/tests/testthat/test-file_exists.R
/usr/lib64/R/library/fs/tests/testthat/test-fs_bytes.R
/usr/lib64/R/library/fs/tests/testthat/test-fs_path.R
/usr/lib64/R/library/fs/tests/testthat/test-fs_perms.R
/usr/lib64/R/library/fs/tests/testthat/test-id.R
/usr/lib64/R/library/fs/tests/testthat/test-is.R
/usr/lib64/R/library/fs/tests/testthat/test-link.R
/usr/lib64/R/library/fs/tests/testthat/test-list.R
/usr/lib64/R/library/fs/tests/testthat/test-path.R
/usr/lib64/R/library/fs/tests/testthat/test-path_package.R
/usr/lib64/R/library/fs/tests/testthat/test-sanitize.R
/usr/lib64/R/library/fs/tests/testthat/test-temp.R
/usr/lib64/R/library/fs/tests/testthat/test-tree.R
/usr/lib64/R/library/fs/tests/testthat/test-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fs/libs/fs.so
/usr/lib64/R/library/fs/libs/fs.so.avx2
/usr/lib64/R/library/fs/libs/fs.so.avx512
