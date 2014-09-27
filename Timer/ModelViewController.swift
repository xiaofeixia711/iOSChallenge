//
//  ModelViewController.swift
//  Timer
//
//  Created by Charles on 14-9-27.
//  Copyright (c) 2014年 Charles. All rights reserved.
//

import UIKit
class ModelController: NSObject, UIPageViewControllerDataSource {
    
    var pageData:[String]=["ViewController","SecondViewController"]
    
    override init() {
        super.init()
        // Create the data model.
    }
    
    func viewControllerAtIndex(index: Int, storyboard: UIStoryboard) -> UIViewController? {
        // Return the data view controller for the given index.
        if (self.pageData.count == 0) || (index >= self.pageData.count) {
            return nil
        }
        
        // Create a new view controller and pass suitable data.
        let dataViewController = storyboard.instantiateViewControllerWithIdentifier(pageData[index]) as UIViewController
        return dataViewController
    }
    
    func pageViewController(pageViewController: UIPageViewController, viewControllerBeforeViewController viewController: UIViewController) -> UIViewController? {
        var vid=viewController.restorationIdentifier
        var index=1
        if (vid=="ViewController"){
            index=0
        }
        if (vid=="SecondViewController"){
            index=1
        }
        if (index == 0) || (index == NSNotFound) {
            return nil
        }
        
        index--
        return self.viewControllerAtIndex(index, storyboard: viewController.storyboard!)
    }
    
    func pageViewController(pageViewController: UIPageViewController, viewControllerAfterViewController viewController: UIViewController) -> UIViewController? {
        var vid=viewController.restorationIdentifier
        var index=1
        if (vid=="ViewController"){
            index=0
        }
        if (vid=="SecondViewController"){
            index=1
        }
        if index == NSNotFound {
            return nil
        }
        
        index++
        if index == self.pageData.count {
            return nil
        }
        return self.viewControllerAtIndex(index, storyboard: viewController.storyboard!)
    }
    
}
