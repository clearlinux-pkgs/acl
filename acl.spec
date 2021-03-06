#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD5BF9FEB0313653A (agruen@gnu.org)
#
Name     : acl
Version  : 2.3.1
Release  : 38
URL      : https://download-mirror.savannah.gnu.org/releases/acl/acl-2.3.1.tar.gz
Source0  : https://download-mirror.savannah.gnu.org/releases/acl/acl-2.3.1.tar.gz
Source1  : https://download-mirror.savannah.gnu.org/releases/acl/acl-2.3.1.tar.gz.sig
Summary  : A library for POSIX Access Control Lists
Group    : Development/Tools
License  : GPL-2.0+ LGPL-2.1
Requires: acl-bin = %{version}-%{release}
Requires: acl-lib = %{version}-%{release}
Requires: acl-license = %{version}-%{release}
Requires: acl-locales = %{version}-%{release}
Requires: acl-man = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : attr-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
__________________________________
Package home: http://savannah.nongnu.org/projects/acl

%package bin
Summary: bin components for the acl package.
Group: Binaries
Requires: acl-license = %{version}-%{release}

%description bin
bin components for the acl package.


%package dev
Summary: dev components for the acl package.
Group: Development
Requires: acl-lib = %{version}-%{release}
Requires: acl-bin = %{version}-%{release}
Provides: acl-devel = %{version}-%{release}
Requires: acl = %{version}-%{release}

%description dev
dev components for the acl package.


%package dev32
Summary: dev32 components for the acl package.
Group: Default
Requires: acl-lib32 = %{version}-%{release}
Requires: acl-bin = %{version}-%{release}
Requires: acl-dev = %{version}-%{release}

%description dev32
dev32 components for the acl package.


%package doc
Summary: doc components for the acl package.
Group: Documentation
Requires: acl-man = %{version}-%{release}

%description doc
doc components for the acl package.


%package lib
Summary: lib components for the acl package.
Group: Libraries
Requires: acl-license = %{version}-%{release}

%description lib
lib components for the acl package.


%package lib32
Summary: lib32 components for the acl package.
Group: Default
Requires: acl-license = %{version}-%{release}

%description lib32
lib32 components for the acl package.


%package license
Summary: license components for the acl package.
Group: Default

%description license
license components for the acl package.


%package locales
Summary: locales components for the acl package.
Group: Default

%description locales
locales components for the acl package.


%package man
Summary: man components for the acl package.
Group: Default

%description man
man components for the acl package.


%prep
%setup -q -n acl-2.3.1
cd %{_builddir}/acl-2.3.1
pushd ..
cp -a acl-2.3.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615912561
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static --enable-nls \
--libexecdir=/usr/lib64 \
--disable-static \
--enable-shared
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-nls \
--libexecdir=/usr/lib64 \
--disable-static \
--enable-shared   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1615912561
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/acl
cp %{_builddir}/acl-2.3.1/doc/COPYING %{buildroot}/usr/share/package-licenses/acl/b0d007e44cc4ad116e706e639fe38bfdc15a00a3
cp %{_builddir}/acl-2.3.1/doc/COPYING.LGPL %{buildroot}/usr/share/package-licenses/acl/e101765734390d664b59325b2d644d80d9a6bd9a
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang acl

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chacl
/usr/bin/getfacl
/usr/bin/setfacl

%files dev
%defattr(-,root,root,-)
/usr/include/acl/libacl.h
/usr/include/sys/acl.h
/usr/lib64/libacl.so
/usr/lib64/pkgconfig/libacl.pc
/usr/share/man/man3/acl_add_perm.3
/usr/share/man/man3/acl_calc_mask.3
/usr/share/man/man3/acl_check.3
/usr/share/man/man3/acl_clear_perms.3
/usr/share/man/man3/acl_cmp.3
/usr/share/man/man3/acl_copy_entry.3
/usr/share/man/man3/acl_copy_ext.3
/usr/share/man/man3/acl_copy_int.3
/usr/share/man/man3/acl_create_entry.3
/usr/share/man/man3/acl_delete_def_file.3
/usr/share/man/man3/acl_delete_entry.3
/usr/share/man/man3/acl_delete_perm.3
/usr/share/man/man3/acl_dup.3
/usr/share/man/man3/acl_entries.3
/usr/share/man/man3/acl_equiv_mode.3
/usr/share/man/man3/acl_error.3
/usr/share/man/man3/acl_extended_fd.3
/usr/share/man/man3/acl_extended_file.3
/usr/share/man/man3/acl_extended_file_nofollow.3
/usr/share/man/man3/acl_free.3
/usr/share/man/man3/acl_from_mode.3
/usr/share/man/man3/acl_from_text.3
/usr/share/man/man3/acl_get_entry.3
/usr/share/man/man3/acl_get_fd.3
/usr/share/man/man3/acl_get_file.3
/usr/share/man/man3/acl_get_perm.3
/usr/share/man/man3/acl_get_permset.3
/usr/share/man/man3/acl_get_qualifier.3
/usr/share/man/man3/acl_get_tag_type.3
/usr/share/man/man3/acl_init.3
/usr/share/man/man3/acl_set_fd.3
/usr/share/man/man3/acl_set_file.3
/usr/share/man/man3/acl_set_permset.3
/usr/share/man/man3/acl_set_qualifier.3
/usr/share/man/man3/acl_set_tag_type.3
/usr/share/man/man3/acl_size.3
/usr/share/man/man3/acl_to_any_text.3
/usr/share/man/man3/acl_to_text.3
/usr/share/man/man3/acl_valid.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libacl.so
/usr/lib32/pkgconfig/32libacl.pc
/usr/lib32/pkgconfig/libacl.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/acl/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libacl.so.1
/usr/lib64/libacl.so.1.1.2301

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libacl.so.1
/usr/lib32/libacl.so.1.1.2301

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/acl/b0d007e44cc4ad116e706e639fe38bfdc15a00a3
/usr/share/package-licenses/acl/e101765734390d664b59325b2d644d80d9a6bd9a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/chacl.1
/usr/share/man/man1/getfacl.1
/usr/share/man/man1/setfacl.1
/usr/share/man/man5/acl.5

%files locales -f acl.lang
%defattr(-,root,root,-)

