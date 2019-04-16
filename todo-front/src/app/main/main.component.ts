import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {Tasklist, Task} from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService) {
  }

  public tasklists: Tasklist[] = [];
  public tasks: Task[] = [];
  public dispTask: Task;
  public loading = true;

  ngOnInit() {
    this.provider.getTasklists().then(
      res => {
        this.tasklists = res;
        this.loading = false;
      }
    );
  }

  getTasks(tasklist: Tasklist) {
    this.provider.getTasks(tasklist).then(res => {
      this.tasks = res;
    });

  }

  getTask(id: number) {
    this.provider.getTask(id).then(res => {
      this.dispTask = res;
    });

  }

}
