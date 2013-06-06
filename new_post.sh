#!/bin/sh
category='设计模式'
title_resource='python设计模式之'
tags='Design Patterns'

while getopts ":c:r:g:s:t:" opt; do
  case $opt in
    c)
    category=$OPTARG
      ;;
    r)
    title_resource=$OPTARG
        ;;
    g)
    tags=$OPTARG
        ;;
    t)
    title=$OPTARG
        ;;
    s)
    slug=$PTARG
        ;;
    ?)
      echo "How to use: $0 [-c category] [-r title_resource] [-g tags] [-t title] [-s slug]" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done
test "x$title" = "x" && read -r -p "Post title [前缀是 ${title_resource}]> " && title=${REPLY}
test "x$slug" = "x" && read -r -p "Post slug [比如abstract-factory]> " && slug=${REPLY}
title=`echo $title | tr "[:upper:]" "[:lower:]"]`
title=`echo $title | tr -d "[:blank:]"`
slug=`echo $slug | tr " " "-"`
fileslug=`echo $slug | tr "-" '_'`
cur_date=`date "+%Y-%m-%d"`
filename="${category}/${fileslug}.md"
author=`git config --get user.name`
echo "Creating preview"
echo "_________________________________"
echo "filename: content/$filename"
echo "title: ${title_resource}${title}"
echo "slug: python-${slug}"
echo "date: ${cur_date}"
echo "category: ${category}"
echo "tags: ${tags}"
echo "_________________________________"
echo ""
read -r -p "Are you ready to create(Y or N) >"
reply=${REPLY}
reply=`echo $reply | tr "[:upper:]" "[:lower:]"]`
test "x$reply" != "xy" && exit 1
cat > "content/"$filename <<EOF
title: ${title_resource}${title}
slug: python-${slug}
date: ${cur_date}
category: ${category}
tags: ${tags}

EOF

$EDITOR "content/"$filename
