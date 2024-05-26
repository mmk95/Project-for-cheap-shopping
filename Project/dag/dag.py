from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def my_python_function(file_name):
    module = __import__(file_name)
    module.execute()


with DAG(
        'Project',
        description='Project DAG',
        schedule_interval=None,
        start_date=datetime(2023, 7, 14), catchup=False
) as dag:
    with TaskGroup(group_id='Scrappings_for_lists_and_urls') as first_scrappings:

        ScrapGroups = PythonOperator(
            task_id='scrapping_groups',
            python_callable=my_python_function,
            op_kwargs={'file_name': 'get_group_names.py'},
            dag=dag,
        )

        ScrapCats = PythonOperator(
            task_id='scrapping_categories',
            python_callable=my_python_function,
            op_kwargs={'file_name': 'get_category_names.py'},
            dag=dag,
        )

        ScrapNames = PythonOperator(
            task_id='scrapping_prod_names',
            python_callable=my_python_function,
            op_kwargs={'file_name': 'get_products_names.py'},
            dag=dag,)

    ScrapUrls = PythonOperator(
        task_id='scrapping_urls',
            python_callable=my_python_function,
            op_kwargs={'file_name': 'get_urls.py'},
        dag=dag,
    )

    with TaskGroup(group_id='scrap_and_transform') as scrap_and_transform:
        with TaskGroup(group_id='Breads') as Breads:
            ScrapBreads = PythonOperator(
                task_id='Scrap',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'bread_scrapping.py'},
                dag=dag,
            )

            TransBreads = PythonOperator(
                task_id='Transform',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'bread_transform.py'},
                dag=dag,
            )

            ScrapBreads >> TransBreads

        with TaskGroup(group_id='Durabels') as Durabels:
            ScrapDur = PythonOperator(
                task_id='Scrap',
                    python_callable=my_python_function,
                op_kwargs={'file_name': 'durabels_scrapping.py'},
                dag=dag,
            )

            TransDur = PythonOperator(
                task_id='Transform',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'durabels_transform.py'},
                dag=dag,
            )

            ScrapDur >> TransDur

        with TaskGroup(group_id='Fruits') as Fruits:
            ScrapFruits = PythonOperator(
                task_id='Scrap',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'fruit_scrapping.py'},
                dag=dag,
            )

            TransFruits = PythonOperator(
                task_id='Transform',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'fruit_transform.py'},
                dag=dag,
            )

            ScrapFruits >> TransFruits

        with TaskGroup(group_id='Meats') as Meats:
            ScrapMeats = PythonOperator(
                task_id='Scrap',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'meat_scrapping.py'},
                dag=dag,
            )

            TransMeats = PythonOperator(
                task_id='Transform',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'meat_transform.py'},
                dag=dag,
            )

            ScrapMeats >> TransMeats

        with TaskGroup(group_id='Milks') as Milks:
            ScrapMilks = PythonOperator(
                task_id='Scrap',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'milk_scrapping.py'},
                dag=dag,
            )

            TransMilks = PythonOperator(
                task_id='Transform',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'milk_transform.py'},
                dag=dag,
            )

            ScrapMilks >> TransMilks

        with TaskGroup(group_id='Spec') as Spec:
            ScrapSpec = PythonOperator(
                task_id='Scrap',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'special_scrapping.py'},
                dag=dag,
            )

            TransSpec = PythonOperator(
                task_id='Transform',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'special_transform.py'},
                dag=dag,
            )

            ScrapSpec >> TransSpec

    create_database_task = PythonOperator(
            task_id='load_group',
            python_callable=my_python_function,
            op_kwargs={'file_name': 'create_database.py'},
            dag=dag,
    )
    with TaskGroup(group_id='Load_menus_into_database') as Load_menus_into_database:

            LoadGroup = PythonOperator(
                task_id='load_group',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_into_sql.py'},
                dag=dag,
            )

            LoadCat = PythonOperator(
                task_id='load_cat',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_into_sql2.py'},
                dag=dag,
            )

            LoadName = PythonOperator(
                task_id='load_name',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_into_sql3.py'},
                dag=dag,
            )
            LoadGroup >> LoadCat >> LoadName

    with TaskGroup(group_id='Load_products_into_database') as Load_products_into_database:

            LoadBreads = PythonOperator(
                task_id='load_breads',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_breads_into_sql.py'},
                dag=dag,
            )

            LoadFruits = PythonOperator(
                task_id='load_fruits',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_fruits_into_sql.py'},
                dag=dag,
            )

            LoadMeats = PythonOperator(
                task_id='load_meats',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_meats_into_sql.py'},
                dag=dag,
            )

            LoadMilks = PythonOperator(
                task_id='load_milks',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_milk_into_sql.py'},
                dag=dag,
            )

            LoadDur = PythonOperator(
                task_id='load_dura',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_dur_into_sql.py'},
                dag=dag,
            )

            LoadSpec = PythonOperator(
                task_id='load_spec',
                python_callable=my_python_function,
                op_kwargs={'file_name': 'load_special_into_sql.py'},
                dag=dag,
            )


first_scrappings >> ScrapUrls >> scrap_and_transform >> create_database_task >> Load_menus_into_database >> Load_products_into_database
