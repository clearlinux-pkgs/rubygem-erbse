#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-erbse
Version  : 0.1.1
Release  : 7
URL      : https://rubygems.org/downloads/erbse-0.1.1.gem
Source0  : https://rubygems.org/downloads/erbse-0.1.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-temple

%description
# Erbse
_An updated version of Erubis._
Erbse compiles an ERB string to a string of Ruby.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n erbse-0.1.1
gem spec %{SOURCE0} -l --ruby > rubygem-erbse.gemspec

%build
export LANG=C
gem build rubygem-erbse.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
erbse-0.1.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/erbse-0.1.1
ruby -v -I.:lib:test test*/test_*.rb
ruby -v -I.:lib:test test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/erbse-0.1.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/CHANGES.md
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/bench.rb
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/bench_context.yaml
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/templates/_footer.html
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/templates/_header.html
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/templates/bench_erb.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/templates/bench_erubis.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/benchmark/templates/bench_eruby.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/erbse.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/lib/erbse.rb
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/lib/erbse/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/lib/erbse/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/test/erbse_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/erbse-0.1.1/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/erbse-0.1.1.gemspec
