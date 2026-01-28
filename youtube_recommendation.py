import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu

df=pd.read_csv("youtube_recommendation_dataset -.csv")
# st.title("Youtube_recommendation_analysis")
with st.sidebar:
    selected=option_menu("Youtube_Recommendation Analytics",["Dataset","Task","Charts"],icons=["cast","bar-chart",],menu_icon=["cast"],orientation="vertical",default_index=0)

if selected == "Dataset":
    st.dataframe(df)

if selected=="Charts":

   charts=st.selectbox("Select the charts",
                            ["1. channel_tittle v/s view_count",
                             "2. channel_tittle v/s like_count",
                            "3. channel_title v/s comment_count",
                              "4. caption",
                             "5. duration",
                             "6. engagement_rate",
                             "7. likes_to_views_ratio",
                             "8. comments_to_views_ratio",
                             "9. caption v/s engagement_rate",
                             "10. caption v/s likes_to_views_ratio",
                             "11. caption v/s comments_to_views_ratio"])

   if charts == "1. channel_tittle v/s view_count":
    fig1,ax1=plt.subplots()
    data1=df.groupby("channel_title")["view_count"].mean().sort_values(ascending=False).head(10)
    ax1.barh(data1.index,data1.values)
    st.title("channel_tittle v/s view_count")
    st.pyplot(fig1)

   if charts == "2. channel_tittle v/s like_count":
    fig2, ax2 = plt.subplots()
    data2 = df.groupby("channel_title")["like_count"].mean().sort_values(ascending=False).head(10)
    ax2.barh(data2.index, data2.values)
    st.title("channel_tittle v/s like_count")
    st.pyplot(fig2)

   if charts == "3. channel_title v/s comment_count":
      fig3, ax3 = plt.subplots()
      data3 = df.groupby("channel_title")["comment_count"].mean().sort_values(ascending=False).head(10)
      ax3.barh(data3.index, data3.values)
      st.title("channel_title v/s comment_count")
      st.pyplot(fig3)

   if charts == "4. caption":
        fig4,ax4=plt.subplots()
        data4=df["caption"].value_counts()
        ax4.pie(data4.values,labels=data4.index.astype(str),autopct="%1.1f")
        st.title("caption_status")
        st.pyplot(fig4)

   if charts =="5. duration":
        fig5,ax5=plt.subplots()
        data5=df.groupby("channel_title")["duration_seconds"].mean().sort_values(ascending=False).head(10)
        ax5.barh(data5.index,data5.values)
        st.title("Channel_title v/s duration")
        st.pyplot(fig5)

   if charts == "6. engagement_rate" :
        fig6,ax6=plt.subplots()
        data6=df.groupby("Title")["engagement_rate"].mean().sort_values(ascending=False).head(10)
        ax6.barh(data6.index,data6.values)
        st.title("Title v/s engagement_rate")
        st.pyplot(fig6)

   if charts == "7. likes_to_views_ratio":
        fig7,ax7=plt.subplots()
        data7=df.groupby("Title")["likes_to_views_ratio"].mean().sort_values(ascending=False).head(10)
        ax7.barh(data7.index,data7.values)
        st.title("Title v/s likes_to_views_ratio")
        st.pyplot(fig7)

   if charts == "8. comments_to_views_ratio":
        fig8, ax8 = plt.subplots()
        data8 = df.groupby("Title")["comments_to_views_ratio"].mean().sort_values(ascending=False).head(10)
        ax8.barh(data8.index, data8.values)
        st.title("Title v/s comments_to_views_ratio")
        st.pyplot(fig8)

   if charts == "9. caption v/s engagement_rate":
        fig9,ax9=plt.subplots()
        data9=df.groupby("caption")["engagement_rate"].mean()
        ax9.pie(data9.values,labels=data9.index.astype(str),autopct="%1.1f")
        st.title("caption v/s engagement_rate")
        st.pyplot(fig9)

   if charts == "10. caption v/s likes_to_views_ratio":
        fig10,ax10=plt.subplots()
        data10=df.groupby("caption")["likes_to_views_ratio"].mean()
        ax10.pie(data10.values,labels=data10.index.astype(str),autopct="%1.1f")
        st.title("caption v/s likes_to_views_ratio")
        st.pyplot(fig10)

   if charts == "11. caption v/s comments_to_views_ratio":
        fig11,ax11=plt.subplots()
        data11=df.groupby("caption")["comments_to_views_ratio"].mean()
        ax11.pie(data11.values,labels=data11.index.astype(str),autopct="%1.1f")
        st.title("caption v/s comments_to_views_ratio")
        st.pyplot(fig11)

if selected == "Task":
    task=st.sidebar.selectbox("Select the Task",
                          ["Task1",
                           "Task2",
                           "Task3",
                           "Task4",
                           "Task5",
                           "Task6",
                           "Task7",
                           "Task8",
                           "Task9",
                           "Task10",
                           "Task11",
                           "Task12",
                           "Task13",
                           "Task14",
                           "Task15"])
    if task == "Task1":
        input=df.shape[0]
        st.write("## Show total number of videos:",input)
        data2 = df["channel_title"].nunique()
        st.write("## Show total number of channels:",data2)
        data3 = df["view_count"].sum()
        st.write("## Show total views:",data3)

    if task =="Task2":
        view = df["view_count"].sort_values(ascending=False).head(10)
        st.write("## Display Top 10 videos by view_count",view)
        title = df["Title"].head(10)
        st.write("## Show columns: Title",title)
        channel_title = df["channel_title"].head(10)
        st.write("## Show columns: Channel_title:",channel_title)

    if task == "Task3":
        like = df.groupby("Title")["like_count"].mean().sort_values(ascending=False).head(10)
        st.write("## Display Top 10 videos by like_count:",like)

    if task == "Task4":
        group_1 = df.groupby("channel_title").size().reset_index(name="Total_Videos").sort_values(by="Total_Videos",ascending=False).head(10)
        st.write("## Display Top 10 channels by number of videos:")
        st.dataframe(group_1)

    if task == "Task5":
        group_2 = df.groupby("category_id").size().reset_index(name="Total_Videos").sort_values(by="Total_Videos",ascending=False).head(10)
        st.write("## Show number of videos per category_id:")
        st.dataframe(group_2)

    if task == "Task6":
        avg_engage = df["engagement_rate"].mean()
        st.write("## Average engagement rate:",avg_engage)
        max_engage = df["engagement_rate"].max()
        st.write("## Maximum engagement rate:",max_engage)
        min_engage = df["engagement_rate"].min()
        st.write("## Minimum engagement rate:",min_engage)

    if task == "Task7":
        group = df.groupby("engagement_rate").size().reset_index(name="Total_Videos").sort_values(by="Total_Videos",ascending=False).head(10)
        st.write("## Show Top 10 videos by engagement_rate:")
        st.dataframe(group)
        data1=df["Title"].value_counts()
        st.write("## Columns:Title",data1)
        data2=df["channel_title"].value_counts()
        st.write("## Columns:Channel_title",data2)
        data3=df["engagement_rate"]
        st.write("## Columns:Engagement_rate",data3)

    if task =="Task8":
        group1 = df.groupby("likes_to_views_ratio").size().reset_index(name="Total_Videos").sort_values(by="Total_Videos").head(10)
        st.write("## Show videos where likes_to_views_ratio is highest:")
        st.dataframe(group1)

    if task =="Task9":
        min_views = st.slider(
            "Select Minimum Views",
            min_value=int(df['view_count'].min()),
            max_value=int(df['view_count'].max()),
            step=10000)

        filtered_views=df[df["view_count"] >= min_views][
            ["Title","channel_title","view_count"]
        ]
        st.write("## Filter Videos by Minimum Views:")
        st.dataframe(filtered_views)

    if task == "Task10":
        New_videos =df[df["video_age_days"] < 30]
        st.write("## New videos (video_age_days < 30):")
        st.dataframe(New_videos)
        st.write("## Count:",New_videos.count())

        Old_videos =df[df["video_age_days"] >= 30]
        st.write("## Old videos (video_age_days >= 30):")
        st.dataframe(Old_videos)
        st.write("## Count:",Old_videos.count())

    if task == "Task11":
        group2 = df.groupby("duration_seconds").size().reset_index(name="Total_Videos").sort_values(by="Total_Videos").head(10)
        st.write("## Show Top 10 longest videos using duration_seconds:")
        st.dataframe(group2)

    if task == "Task12":
        data_2=df["caption"].value_counts().reset_index()
        data_2.columns=["Caption_Available","Total_Videos"]
        st.dataframe(data_2)

    if task == "Task13":
        group3=df.groupby("category_id")["view_count"].mean().sort_values()
        st.write("## Show average views per category:",group3)

    if task == "Task14":
        group4=df.groupby("channel_title")["like_count"].mean().sort_values(ascending=False).head(10)
        st.write("## Show Top 10 channels by average likes:")
        st.dataframe(group4)


    if task == "Task15":
        search=st.text_input("Enter keyword to search in title:")
        if search:
            searched_df=df[df["Title"].str.contains(search,case=False,na=False)]
            st.write("## Search Videos by Title")
            st.dataframe(searched_df[["Title","channel_title","view_count"]])

