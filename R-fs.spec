#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-fs
Version  : 1.6.4
Release  : 59
URL      : https://cran.r-project.org/src/contrib/fs_1.6.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fs_1.6.4.tar.gz
Summary  : Cross-Platform File System Operations Based on 'libuv'
Group    : Development/Tools
License  : MIT
Requires: R-fs-lib = %{version}-%{release}
Requires: R-fs-license = %{version}-%{release}
BuildRequires : buildreq-R

%description
on top of the 'libuv' C library.

%package lib
Summary: lib components for the R-fs package.
Group: Libraries
Requires: R-fs-license = %{version}-%{release}

%description lib
lib components for the R-fs package.


%package license
Summary: license components for the R-fs package.
Group: Default

%description license
license components for the R-fs package.


%prep
%setup -q -n fs
pushd ..
cp -a fs buildavx2
popd
pushd ..
cp -a fs buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714065185

%install
export SOURCE_DATE_EPOCH=1714065185
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-fs
cp %{_builddir}/fs/inst/COPYRIGHTS %{buildroot}/usr/share/package-licenses/R-fs/fba7bce5197277bd54f0fd6a8a9c1bdd2a6cad77 || :
cp %{_builddir}/fs/src/libuv-1.44.2/LICENSE %{buildroot}/usr/share/package-licenses/R-fs/995532b42e0ad16d5ee90d1538f3d74a91fa76e6 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fs/COPYRIGHTS
/usr/lib64/R/library/fs/DESCRIPTION
/usr/lib64/R/library/fs/INDEX
/usr/lib64/R/library/fs/LICENSE
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
/usr/lib64/R/library/fs/help/figures/logo.png
/usr/lib64/R/library/fs/help/fs.rdb
/usr/lib64/R/library/fs/help/fs.rdx
/usr/lib64/R/library/fs/help/paths.rds
/usr/lib64/R/library/fs/html/00Index.html
/usr/lib64/R/library/fs/html/R.css
/usr/lib64/R/library/fs/tests/spelling.R
/usr/lib64/R/library/fs/tests/testthat.R
/usr/lib64/R/library/fs/tests/testthat/_snaps/tree.md
/usr/lib64/R/library/fs/tests/testthat/blns.txt.xz
/usr/lib64/R/library/fs/tests/testthat/helper.R
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
/V3/usr/lib64/R/library/fs/libs/fs.so
/V4/usr/lib64/R/library/fs/libs/fs.so
/usr/lib64/R/library/fs/libs/fs.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-fs/995532b42e0ad16d5ee90d1538f3d74a91fa76e6
/usr/share/package-licenses/R-fs/fba7bce5197277bd54f0fd6a8a9c1bdd2a6cad77
